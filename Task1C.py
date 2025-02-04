from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()
desired_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)
alphasort_stations = sorted(desired_stations)
print(alphasort_stations)


