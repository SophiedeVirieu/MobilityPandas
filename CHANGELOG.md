# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.12.0a] - 2025-06-03

### Changed
Adapted MobilityPandas to :

  pymeos     : 1.2.0  
  geopandas  : 1.0.1  
  pandas     : 2.2.3  
  shapely    : 2.0.6  
  
  <!-- fiona      : 1.10.1
  numpy      : 1.26.4
  rtree      : 1.4.0
  pyproj     : 3.6.1
  matplotlib : 3.9.2
  mapclassify: 2.5.0
  geopy      : 2.4.1
  holoviews  : 1.20.2
  hvplot     : 0.11.3
  geoviews   : 1.12.0
  stonesoup  : 1.6 
  python     : 3.9.21 -->

### Fixed

Updated internal code to answer breaking changes introduced in recent versions of upstream libraries:

- Pandas 2.2.3: `iteritems()` became `items()`.
- Shapely 2.0.6: geometry attributes restructured
- GeoPandas 1.0.1: deprecated `GeoDataFrame.append()` removed
- MobilityDB / PyMEOS: class attributes such as `.timestamp` have become methods.
- trajectory module: `from_arrays()` suppressed. The constructor of `TGeomPointInst` class was used instead.
- trajectory\_generalizer: `simplify()` became `simplify_douglas_peucker()`.

### Notes
- Internal changes are **not backward-compatible** for custom subclassing or extensions relying on old trajectory internals.
- No user-facing API changes.

## [0.12.0b] - 2025-09-05

### Changed

The trajectory constructor was optimized

### Added

- A benchmark of the new trajectory constructor  
- Functions Douglas-Peucker with time consideration, minimum distance, minimum time delta and hausdorff distance  
- A benchmark of MobilityPandas versus MovingPandas  

---
