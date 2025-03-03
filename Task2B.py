from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Print station and latest level for stations with levels over 0.8 
    tol = 0.8

    tol_stations = stations_level_over_threshold(stations, tol)

    for station in tol_stations:
        print(station[0].name, station[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()

