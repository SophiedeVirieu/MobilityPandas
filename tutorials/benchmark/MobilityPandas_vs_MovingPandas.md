# Benchmark of MovingPandas vs. MobilityPandas on AIS Trajectories

## Abstract
This document presents a benchmark comparing **MovingPandas** with **MobilityPandas** (using **PyMEOS** backend) on AIS trajectory data. We measure performance, fidelity, speed, and memory usage when applying different trajectory functions over three dataset sizes.

## Table of Contents
1. [Introduction](#introduction)  
2. [Data](#data)  
3. [Environment](#environment)  
4. [Methods](#methods)  
   1. [Coordinate Projection](#coordinate-projection)  
   2. [Trajectory Construction](#trajectory-construction)  
   3. [Functions Applied](#functions-applied)  
   4. [Benchmark Protocol](#benchmark-protocol)  
5. [Metrics](#metrics)  
6. [Results](#results)  
   1. [Small Dataset](#small-dataset)  
   2. [Medium Dataset](#medium-dataset)  
   3. [Large Dataset](#large-dataset)  
   4. [Overall Ranking](#overall-ranking)  
7. [Discussion](#discussion)  
8. [Conclusion](#conclusion)  
9. [Code and Data Availability](#code-and-data-availability)  
10. [References](#references)  

---

## Introduction
Marine vessel traffic is routinely recorded via Automatic Identification System (AIS), producing high-frequency spatio-temporal point streams. Here, we benchmark two Python-based libraries:
- **MovingPandas**: builds a `TrajectoryCollection` of `Trajectory` objects.  
- **MobilityPandas**: constructs a `TGeomPointSeq` via the PyMEOS backend. <!--for vectorized operations.   -->

We compare them on:
- Simplification  <!-- (with Douglas–Peucker algorithm),   -->
- Other trajectory functions  <!-- (TODO: list other functions),   -->
over datasets of different sizes.

## Data
- **Source**: AIS vessel positions provided by the Danish Maritime Authority : https://web.ais.dk/aisdata/  
- **Attributes**: `mmsi`, `timestamp`, `longitude`, `latitude`.  
- **Sizes**:  
  - **Small**: ~TODO points  
  - **Medium**: ~TODO points  
  - **Large**: ~TODO points  
- **Preprocessing**:  
  1. Filter out duplicates, invalid timestamps, and non‐vessel points.  
  2. Sort by `mmsi`, then `timestamp`.  
  3. Reprojection of the longitude/latitude points (EPSG:4326) to **EPSG:25832** (UTM zone 32N) for metric distance calculations:
```python
gdf = gdf.set_crs("EPSG:4326").to_crs("EPSG:25832")
```
  4. 
  
  
  TODO

## Environment
- **Hardware**:  
  - CPU: TODO (e.g., Intel Core i7‑9700K @ 3.6 GHz)  
  - RAM: TODO GB  
  - Storage: TODO SSD  
- **Software**:  
  - Python: TODO (e.g., 3.11.2)  
  - MovingPandas: TODO (e.g., 0.15.2)  
  - MobilityPandas: TODO (e.g., 0.3.1)  
  - pymeos: TODO (e.g., 0.7.0)  
  - GeoPandas: TODO  
  - pandas: TODO  
  - Other dependencies: TODO  

## Methods

### Trajectory Construction
1. **MovingPandas**  
   ```python
   from movingpandas import TrajectoryCollection
   tc = TrajectoryCollection(gdf, traj_id="mmsi", t="timestamp")
   ```

2. **MobilityPandas**  
   ```python
   import mobilitypandas as mp
   # TODO: explain the new `from_arrays` method
   tc_mp = mp.TGeomPointSeq.from_geodataframe(gdf, id_col="mmsi", time_col="timestamp")
   # Alternatively:
   tc_mp2 = mp.TGeomPointSeq.from_arrays(ids, times, xs, ys)
   ```

### Functions Applied
- **Trajectory simplification**: Douglas–Peucker  
  - Parameter ε = TODO meters  
  - Implemented via `.simplify()` in both libraries.  
- **Other functions**:  
  - TODO: list and describe  

### Benchmark Protocol
- Each function is executed **8 times** per dataset and library.  
- We discard the **minimum** and **maximum** runtimes as outliers.  
- We compute **mean** and **standard deviation** over the remaining 6 runs.  
- Memory usage is measured via TODO tool (e.g., `memory_profiler`).  

## Metrics
We record for each run:
1. **Execution time** (s)  
2. **Memory usage** (peak RAM, MB)  
3. **Spatial–temporal distortion**  
4. **Points retained** (for simplification)  
5. **Trajectory length difference** (m)  

## Results

### Small Dataset
- **MovingPandas**  
  - Points retained: TODO  
  - Time: TODO ± TODO s  
  - Memory: TODO MB  
  - Distortion: TODO  
  - Length diff: TODO m  
- **MobilityPandas**  
  - Points retained: TODO  
  - Time: TODO ± TODO s  
  - Memory: TODO MB  
  - Distortion: TODO  
  - Length diff: TODO m  

![Figure 1: Small Dataset Results](TODO/path/to/figure1.png)  
*Figure 1. Performance comparison on the small dataset.*

### Medium Dataset
- **MovingPandas**: TODO  
- **MobilityPandas**: TODO  

![Figure 2: Medium Dataset Results](TODO/path/to/figure2.png)  

### Large Dataset
- **MovingPandas**: TODO  
- **MobilityPandas**: TODO  

![Figure 3: Large Dataset Results](TODO/path/to/figure3.png)  

### Overall Ranking
| Criterion                 | Winner            | Notes                    |
|---------------------------|-------------------|--------------------------|
| Simplification Speed      | TODO              |                          |
| Memory Efficiency         | TODO              |                          |
| Fidelity (low distortion) | TODO              |                          |
| Scalability               | TODO              |                          |

## Discussion
- Trade‐off between execution speed and spatial fidelity.  
- Impact of pymeos backend on vectorized operations.  
- TODO: interpret results, link to theory and prior work.

## Conclusion
Summarize main findings:
- MobilityPandas outperforms on …  
- MovingPandas remains preferable when …

## Code and Data Availability
- **Notebook**: [Benchmark Analysis (GitHub link)](TODO link)  
- **Datasets**:  
  - Small: TODO URL  
  - Medium: TODO URL  
  - Large: TODO URL  

## References
1. Douglas, D., & Peucker, T. (1973). Algorithms for the Reduction of the Number of Points Required to Represent a Digitized Line or Its Caricature. *Cartographica*.  
2. Karagiorgou, S., & Pfoser, D. (2020). MOVINGPANDAS: Trajectory Analytics in Python. *Journal of Open Source Software*.  
3. TODO: other relevant citations.

---