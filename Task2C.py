from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level


def run():

    # Build list of stations
    stations = build_station_list()

    N = 10

    highest_stations = stations_highest_rel_level(stations, N)

    print(highest_stations)

    
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")