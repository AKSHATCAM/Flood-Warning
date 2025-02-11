from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river

def runE():
    stations = build_station_list()
    List = rivers_by_station_number(stations, 9)
    print(List)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    runE()