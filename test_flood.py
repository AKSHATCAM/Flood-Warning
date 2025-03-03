# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level, risk

def test_stations_level_over_threshold():

    stations = build_station_list()
    update_water_levels(stations)
    tol_stations = stations_level_over_threshold(stations, 0.8)

    #assert type(tol_stations[3][1]) == int

def test_stations_highest_rel_level():

    stations = build_station_list()
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 10)

    assert len(highest_stations) >= 10

def test_risk():

    stations = build_station_list()
    update_water_levels(stations)
    coeff = risk(stations[2])
    
    assert coeff <= 5
    assert coeff >= 0
    #assert type(coeff) == int
