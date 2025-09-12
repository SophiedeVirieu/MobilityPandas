## Imports

import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point

from geopandas import GeoDataFrame
import zipfile

import sys
import os
sys.path.append("../..")
import movingpandas as mpd

import warnings
import numpy as np
warnings.simplefilter("ignore")
from pyproj import Transformer
from collections import Counter
from itertools import compress

import pymeos
from pymeos.mixins.simplify import TSimplifiable
from pymeos import TGeomPointSeq
import time
from memory_profiler import memory_usage

pymeos.pymeos_initialize()

## Variables

zip_path = ['data/aisdk-2025-07-11.zip', 'data/aisdk-2025-07-12.zip']
csv_filename = ['aisdk-2025-07-11.csv', 'aisdk-2025-07-12.csv']

sizes = {'small': 100000, 'medium': 1000000, 'large': 4000000}

list_of_selected_mmsi = [2579999, 219236000, 2190049, 2190068, 2190048, 2190069, 257076860, 258092000, 2190067, 235108534, 
                         2655148, 259490000, 265859000, 2190071, 219022903, 2190051, 2190073, 219007781, 247389200, 3638]


## Functions

def mem_and_cpu_time(f, n=4, arg=None):

    argNone = True
    try:
        if arg is not None:
            argNone = False
    except:
        argNone = False

    if argNone:
        mem_usage = memory_usage((f), interval=0.01)
    else:
        mem_usage = memory_usage((f, (arg,)), interval=0.01)

    mem_used = max(mem_usage) - min(mem_usage)

    times = []
    for _ in range(n):
        start = time.process_time()
        if argNone:
            out = f()
        else:
            out = f(arg)
        end = time.process_time()

        cpu_time = end - start
        times.append(cpu_time)

    times.pop(times.index(max(times)))
    times.pop(times.index(min(times)))
    mean_t = np.mean(times)
    std_t = np.std(times)


    print(f"Function {f.__name__}:")
    print(f"CPU time: {mean_t:.6f} sec ± {std_t:.6f} sec")
    print(f"Memory usage: {mem_used:.2f} MiB\n")

    return out


def find_mmsi():
    global list_of_selected_mmsi
    list_of_selected_mmsi = []


    mmsi_counter = Counter()

    for i in range(len(zip_path)):
        with zipfile.ZipFile(zip_path[i]) as archive:
            with archive.open(csv_filename[i]) as file:
                for chunk in pd.read_csv(
                    file,
                    usecols=['MMSI'],
                    chunksize=100_000
                ):
                    counts = chunk['MMSI'].value_counts()
                    mmsi_counter.update(counts.to_dict())

    list_of_selected_mmsi = [mmsi for mmsi, _ in mmsi_counter.most_common(20)]
    

def extraction(chosen_size):
    with zipfile.ZipFile(zip_path[0]) as archive:        
        with archive.open(csv_filename[0]) as file:
            df = pd.read_csv(file, usecols=['# Timestamp', 'MMSI', 'Latitude', 'Longitude'], nrows=sizes[chosen_size])

    df.rename(columns={'# Timestamp': 't', 'MMSI': 'mmsi', 'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)
    df = df[df['lat'] <= 90] # default latitude = 91°
    df = df.sort_values(['mmsi', 't'])
    df = df.drop_duplicates(subset=['mmsi', 't'], keep='last')

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:25832", always_xy=True)

    df[['x', 'y']] = df.apply(
        lambda row: pd.Series(transformer.transform(row['lon'], row['lat'])),
        axis=1
    )
    df = df.drop(columns=['lat', 'lon'])

    return df



def extraction2():
    # we take two days of the 50 richest trajectories

    dfs = []

    for i in range(len(zip_path)):
        with zipfile.ZipFile(zip_path[i]) as archive:
            with archive.open(csv_filename[i]) as file:
                for chunk in pd.read_csv(
                    file,
                    usecols=['# Timestamp', 'MMSI', 'Latitude', 'Longitude'],
                    chunksize=50_000
                ):
                    filtered = chunk[chunk['MMSI'].isin(list_of_selected_mmsi)]
                    if not filtered.empty:
                        dfs.append(filtered)

    df = pd.concat(dfs, ignore_index=True)

    df.rename(columns={'# Timestamp': 't', 'MMSI': 'mmsi', 'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)
    df = df[df['lat'] <= 90] # default latitude = 91°
    df = df.sort_values(['mmsi', 't'])
    df = df.drop_duplicates(subset=['mmsi', 't'], keep='last')

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:25832", always_xy=True)

    df[['x', 'y']] = df.apply(
        lambda row: pd.Series(transformer.transform(row['lon'], row['lat'])),
        axis=1
    )
    df = df.drop(columns=['lat', 'lon'])

    global nb_points
    nb_points = df.shape[0]

    return df

def construction_TC(df):
    df1 = df.copy()
    df1['geometry'] = [Point(x, y) for x, y in zip(df1['x'], df1['y'])]
    gdf = GeoDataFrame(df1, geometry='geometry')
    gdf.set_crs(epsg=25832, inplace=True)
    gdf['t'] = pd.to_datetime(gdf['t'])

    return mpd.TrajectoryCollection(gdf, traj_id_col='mmsi', t='t')


def construction_TG(df):

    df3 = df.copy()
    df3['t'] = pd.to_datetime(df3['t'])

    tr = (df3.groupby('mmsi')
        .apply(lambda traj: TGeomPointSeq.from_arrays(
            t = traj['t'].dt.strftime('%Y-%m-%d %H:%M:%S').values,
            x = traj['x'].values, 
            y = traj['y'].values,
            upper_inc=True,
        ))
        .rename('trajectory')
    ).to_frame()

    return tr['trajectory'].apply(
        lambda seq: TGeomPointSeq.from_instants(seq.instants(), upper_inc=True)
    ).to_frame(name='trajectory')


def simplify_with(transf1):
    simplified_with = transf1.trajectory.apply(
        lambda x: TSimplifiable.simplify_douglas_peucker(x, distance=1, synchronized=False)
    )

    return simplified_with



## Program

# find_mmsi()
# print(list_of_selected_mmsi)