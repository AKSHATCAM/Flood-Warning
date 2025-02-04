from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

p = (52.2053, 0.1218)
stations = build_station_list()
print(stations_by_distance(stations, p)[:10])