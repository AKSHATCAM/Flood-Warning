from floodsystem.stationdata import build_station_list, update_water_levels

def highest_rel_level(stations, N):
    full_list = []
    for station in stations:
        level = station.relative_water_level()
        if station.typical_range_consistent() and level is not None:
            full_list.append((station, level))
    full_list.sort(key=lambda x: x[1], reverse=True)
    station_list = [num[0] for num in full_list]
    return station_list[:N]
