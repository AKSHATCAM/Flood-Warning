
def stations_level_over_threshold(stations, tol):
    full_list = []
    for station in stations:
        if station.typical_range != None and station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                station_tuple = (station.name, station.relative_water_level())
                full_list.append(station_tuple)
    full_list.sort(key=lambda x: x[1], reverse=True)
    return full_list

def stations_highest_rel_level(stations, N):
    full_list = stations_level_over_threshold(stations, 0)
    object_list = []
    for i in full_list[:N]:
        object_list.append(i[0])
        for station in stations:
            if station.name == i[0]:
                object_list.append(station)
    return object_list

        

