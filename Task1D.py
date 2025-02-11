from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def runD():
    stations = build_station_list()
    print("The number of rivers with at least one monitoring station is",len(rivers_with_station(stations)))
    print() #leave a space bewtween lines"
    first_10_rivers = rivers_with_station(stations) [:10]
    print("The first 10 of these rivers", first_10_rivers)

    for river in ["River Aire", "River Cam", "River Thames"]: 
        name_list = [] 
        print("The stations on {} are:".format(river))
        for station in stations_by_river(stations)[river]:
            name_list += [station.name] 
        name_list.sort() 
        print(name_list)
        print()
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    runD()