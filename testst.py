from floodsystem.stationdata import build_station_list, update_water_levels


stations = build_station_list()
update_water_levels(stations)
full_list = []
for station in stations:
    level = station.relative_water_level()
    if station.typical_range_consistent() and level is not None:
        full_list.append((station, level))

full_list.sort(key=lambda x: x[1], reverse=True)
# want to iterate throught the first N elements of the list, and then extract the 0th element of each tuple
N = 10
station_list = [num[0] for num in full_list]
for station in station_list[:N]:
    print(station.name, station.relative_water_level())