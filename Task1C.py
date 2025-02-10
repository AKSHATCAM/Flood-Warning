from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine

def run():
    stations = build_station_list()
    desired_stations = stations_within_radius(stations, (52.2053, 0.1218), 10)
    alphasort_stations = sorted(desired_stations)
    print(alphasort_stations)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


