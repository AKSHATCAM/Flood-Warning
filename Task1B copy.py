from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

# Define Cambridge city centre coordinates
pp = (52.2053, 0.1218)

# Build the station list
stations = build_station_list()

# Get the list of (station, distance) tuples
list_with_distances = stations_by_distance(stations, pp)

list_with_names = []
town_list = []
closest = []
furthest = []

# Extract station names
for i in list_with_distances:
    list_with_names.append(i[0])

# Extract corresponding towns
for i in list_with_names:
        town_found = False
        for station in stations:
            if station.name == i:
                town_list.append(station.town if station.town else "unknown")
                town_found = True
                break
        if not town_found:
            town_list.append("unknown")



# Combine the two lists into a list of tuples

for i in list_with_distances[:10]:
    closest.append((i[0],town_list[list_with_names.index(i[0])], i[1]))

for i in list_with_distances[-10:]:
    furthest.append((i[0],town_list[list_with_names.index(i[0])], i[1]))


print(furthest)
print(len(furthest))