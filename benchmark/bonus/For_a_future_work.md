### Trajectory Construction

Trajectory construction is a necessary step before using any of the following methods. This part benchmarks the construction times of TGeomPointSeq (PyMEOS object) and TrajectoryCollection (MovingPandas object).


The construction of the trajectory simplifies it a little bit, by deleting the aligned points. In MovingPandas, we build the trajectories using `TrajectoryCollection` constructor. In MobilityPandas, we build the trajectories using the `from_arrays` method, then `from_instants` method. [This protocol](https://github.com/SophiedeVirieu/MobilityPandas/blob/update/mpandas-0.12/tutorials/benchmark/demo_from_arrays.md) is faster than constructing the instants individually and then using `from_instants`.
In this way, we build a dataframe of `TGeomPoint` objects.  

**Small dataset (100,000 points)**  

  percentage of kept points:   MovingPandas: 96.61%,    MobilityPandas: 92.14%  
  <img src=diagrams/cons_t_small.png width="450">   |    <img src=diagrams/cons_m_small.png width="450"> 

**Medium dataset (1,000,000 points)**  

  percentage of kept points:    MovingPandas: 99.95%,     MobilityPandas: 89.79%  
  <img src=diagrams/cons_t_med.png width="450">     |    <img src=diagrams/cons_m_med.png width="450">   

**Large dataset (5,000,000 points)**  

  percentage of kept points:    MovingPandas: 99.99%,     MobilityPandas: 89.3%  
  <img src=diagrams/cons_t_big.png width="450">     |    <img src=diagrams/cons_m_big.png width="450">   

**Partial conclusion**  
PyMEOS is more efficient than MovingPandas regarding execution time, memory efficiency and simplification. This results will be injected in some of the following results.

### Sampling with respect to a time interval

Here we reduce the trajectories using `GeoPandas` methods instead of `MovingPandas`, and then we buid a MovingPandas `TrajectoryCollection`.  

**Small Dataset (100,000 points)**  
- **GeoPandas**  
  - Points retained: 33.4 %   
  - Maximum length difference: 461.73 m, average length difference: 2.24 m  
- **PyMEOS**  
  - Points retained: 25.05 %  
  - Maximum length difference: 65,514.39 m, average length difference: 50.56 m  

- **Time and memory performance**  

  <img src=diagrams/samcalc_t_small.png width="450">  <img src=diagrams/samcalc_m_small.png width="450">
  <img src=diagrams/samall_small.png width="450">  

**Medium Dataset (1,000,000 points)**  
- **GeoPandas**  
  - Points retained: 30.22 %   
  - Maximum length difference: 207,602.68 m, average length difference: 160.59 m  
- **PyMEOS**  
  - Points retained: 32.38 %  
  - Maximum length difference: 643,439.11 m, average length difference: 386.98 m  

- **Time and memory performance**

  <img src=diagrams/samcalc_t_med.png width="450">         <img src=diagrams/samcalc_m_med.png width="450"> 
  <img src=diagrams/samall_med.png width="450"> 

**Large Dataset (5,000,000 points)**  
- **GeoPandas**  
  - Points retained: 29.5 %     
  - Maximum length difference: 6,188,855.96 m, average length difference: 2162.19 m  

- **PyMEOS**  
  - Points retained: 33.56 %  
  - Maximum length difference: 7,308,377.02 m, average length difference: 2429.86 m  

  <img src=diagrams/samcalc_t_big.png width="450">         <img src=diagrams/samcalc_m_big.png width="450"> 
  <img src=diagrams/samall_big.png width="450"> 


**Partial conclusion**  

We remark that the PyMEOS function does not keep the last point. GeoPandas is as a consequence the most fidelitous. For large datasets, GeoPandas keeps less points than PyMEOS. The most efficient regarding execution time and memory usage is again PyMEOS.

### Fréchet distance

Here we use Shapely instead of MovingPandas. It modifies the construction time of the trajectories, so that PyMEOS is slower for constructing the trajectories, especially for small datasets. This is taken into account in the execution time for all process.  
The two libraries give the same distance results, so we only show time and memory performance. 

**Small Dataset (100,000 points)**  

  Memory usage is negligible for both libraries.  
  <img src=diagrams/fdcalc_t_small.png width="450">
  <img src=diagrams/fdall_small.png width="450"> 

**Medium Dataset (1,000,000 points)**  

  <img src=diagrams/fdcalc_t_med.png width="450">         <img src=diagrams/fdcalc_m_med.png width="450">
  <img src=diagrams/fdall_med.png width="450"> 

**Large Dataset (4,000,000 points)**  

  <img src=diagrams/fdcalc_t_big.png width="450">         <img src=diagrams/fdcalc_m_big.png width="450">
  <img src=diagrams/fdall_big.png width="450"> 

**Twenty trajectories dataset**  

### About MobilityPandas optimization

After having tested custom functions that mimetize MobilityPandas on a "medium" dataset with basic Douglas-Peucker algorithm, it appears that about 80% of the execution time is due to the second conversion : TGeomPointSeq to TrajectoryCollection, 19% for the first conversion, and 1% for calculation. On the other hand, this second conversion can be made faster by converting all the trajectories together instead of one by one. See the file [optimization.ipynb](optimization.ipynb).