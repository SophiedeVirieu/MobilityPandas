# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.12.0] - 2025-06-03

### Fixed
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
stonesoup  : 1.6 -->

### Changed

Updated internal code to answer breaking changes introduced in recent versions of upstream libraries:

- Pandas 2.2.3: `iteritems()` became `items()`.
- Shapely 2.0.6: geometry attributes restructured
- GeoPandas 1.0.1: deprecated `GeoDataFrame.append()` removed
- MobilityDB / PyMEOS: class attributes such as `.timestamp` have become methods.
- Trajectory module: `from\_arrays()` became `from\_base\_temporal()`.
- trajectory\_generalizer: `simplify()` became `simplify\_douglas\_peucker()`.

### Notes
- Internal changes are **not backward-compatible** for custom subclassing or extensions relying on old trajectory internals.
- No user-facing API changes.
- Some fixes are still in progress.

---

