"""Unit test for geo.py file"""
from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_within_radius, stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number


def test_rivers_with_station():
    stations = build_station_list()
    List = rivers_with_station(stations)
    Sample = ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alphin Brook', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop']
    assert List[0:10] == Sample


def test_rivers_by_station_number():

    stations = build_station_list()
    List = rivers_by_station_number(stations, 9)
    assert List == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 30), ('River Derwent', 26), ('River Aire', 24), ('River Calder', 23), ('River Severn', 21), ('River Stour', 20), ('River Colne', 19)]

