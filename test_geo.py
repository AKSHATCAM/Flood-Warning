"""Unit test for geo.py file"""
from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_within_radius, stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number

def test_stations_within_radius():
    stations = build_station_list()
    assert type(stations_within_radius(stations, (52.2053, 0.1218), 10)) == list
    assert sorted(stations_within_radius(stations, (52.2053, 0.1218), 10)) == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    
test_stations_within_radius()

def test_stations_by_distance():
    stations = build_station_list()
    List = stations_by_distance(stations, (52.2053, 0.1218))
    assert len(List) == len(stations)
    assert type(List) == list
    

def test_rivers_with_station():
    stations = build_station_list()
    List = rivers_with_station(stations)
    assert len(List) == 1052

def test_stations_by_river():
    stations = build_station_list() 
    rivers = stations_by_river(stations) 
    assert len(rivers.keys()) == len(rivers_with_station(stations))
    assert type(rivers) == dict


def test_rivers_by_station_number():
    stations = build_station_list()
    List = rivers_by_station_number(stations, 9)
    assert len(List) >= 9
    assert type(List) == list

