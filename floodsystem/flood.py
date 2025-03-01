
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
def stations_level_over_threshold(stations, tol):
    full_list = []
    for station in stations:
        level = station.relative_water_level()
        if station.typical_range_consistent() and level is not None:
            if level > tol:
                full_list.append((station.name, level))
    
    # Sort the list in descending order based on water level
    full_list.sort(key=lambda x: x[1], reverse=True)
    
    return full_list

    
def stations_highest_rel_level(stations, N):
    full_list = []
    for station in stations:
        level = station.relative_water_level()
        if station.typical_range_consistent() and level is not None:
            full_list.append((station, level))

    full_list.sort(key=lambda x: x[1], reverse=True)
    station_list = [num[0] for num in full_list]
    return station_list[:N]
