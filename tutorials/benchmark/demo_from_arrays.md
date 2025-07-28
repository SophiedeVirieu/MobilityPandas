
# Quick Comparison: `from_instants` vs `from_arrays` in PyMEOS
## Introduction

This benchmark compares two methods for constructing trajectories using PyMEOS. 
`from_instants` is already implemented in PyMEOS; `from_arrays` is currently not yet implemented in the library.  
With `from_instants`, we build TGeomPointInsts individually and then call `from_instants` for building the trajectory as a TGeomPointSeq object. With `from_arrays`, we build a sequence of instants calling `from_arrays`, and then we call `from_instants` for building the trajectory as a TGeomPointSeq object. The resulting objects are the same with the two methods.

We use AIS data (https://web.ais.dk/aisdata/)  

The used code can be seen here: https://github.com/SophiedeVirieu/MobilityPandas/blob/update/mpandas-0.12/tutorials/benchmark/demo_from_arrays.ipynb  

## Results
### Large dataset (5 million rows)

| Execution time | Memory usage |
|---------------|-------------|
| ![alt text](from_arrays_t_big.png) | ![alt text](from_arrays_m_big.png) |

### Medium dataset (1 million rows)

| Execution time | Memory usage |
|---------------|-------------|
|  ![alt text](from_arrays_t_med.png)  |  ![alt text](from_arrays_m_med.png)  |

### Small dataset (100 thousands rows)

| Execution time | Memory usage |
|---------------|-------------|
|  ![alt text](from_arrays_t_small.png)  |  ![alt text](from_arrays_m_small.png)  |

## Conclusion 

`from_arrays` method is significantly more efficient than `from_instants`, especially on large datasets.  
