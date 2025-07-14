
# Quick Comparison: `from_instants` vs `from_arrays` in PyMEOS

This benchmark compares two methods for constructing trajectories using PyMEOS.  
`from_instants` is already implemented in PyMEOS; `from_arrays` is currently not yet implemented in the library.

We use AIS data (https://web.ais.dk/aisdata/)  

The used code can be seen here: https://github.com/SophiedeVirieu/MobilityPandas/blob/update/mpandas-0.12/tutorials/benchmark/demo_from_arrays.ipynb  


## Big dataset (20 million rows)

| Execution time | Memory usage |
|---------------|-------------|
| ![instants](image.png) | ![arrays](image-1.png) |

## Medium dataset (5 million rows)

| Execution time | Memory usage |
|---------------|-------------|
|  ![from_instants_medium](image-5.png)  |  ![from_arrays_medium](image-6.png)  |

## Small dataset (1 million rows)

| Execution time | Memory usage |
|---------------|-------------|
|  ![from_instants_small](image-2.png)  |  ![from_arrays_small](image-3.png)  |

## Conclusion (preliminary)

`from_arrays` is significantly faster, especially on big datasets.  
