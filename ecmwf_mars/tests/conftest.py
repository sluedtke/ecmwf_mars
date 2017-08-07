#!/usr/bin/python
#
######################################################################

#       Filename: conftest.py

#       Author: Stefan Luedtke

######################################################################

import pytest

######################################################################


@pytest.fixture(scope="function")
def example_1():
    """
    Fixture that is the python equivalent to the example_1.txt.
    """
    example_1 = {
        "class": "ei",
        "dataset": "interim",
        "date": "1979-01-01/to/1979-01-31",
        "expver": "1",
        "grid": "0.75/0.75",
        "levtype": "sfc",
        "param": "168.128",
        "step": "0",
        "stream": "oper",
        "time": "00:00:00",
        "type": "an",
        "target": "output"
    }
    return(example_1)
# -----------------------------------------------------------


@pytest.fixture(scope="function")
def example_2():
    """
    Fixture that is the python equivalent to the example_2.txt.
    """
    example_2 = {
        "class": "ei",
        "dataset": "interim",
        "date": "1979-01-01/to/1979-02-28",
        "expver": "1",
        "grid": "0.75/0.75",
        "levtype": "sfc",
        "param": "63.162/168.128",
        "step": "0",
        "stream": "oper",
        "time": "00:00:00",
        "type": "an",
        "target": "output"
    }
    return(example_2)
# -----------------------------------------------------------


@pytest.fixture(scope="function")
def example_3():
    """
    Fixture that is the python equivalent to the example_3.txt.
    """
    example_3 = {
        "class": "ei",
        "dataset": "interim",
        "date": "1979-01-01/to/1980-12-31",
        "expver": "1",
        "grid": "0.75/0.75",
        "levtype": "sfc",
        "param": "63.162/168.128",
        "step": "0",
        "stream": "oper",
        "time": "00:00:00",
        "type": "an",
        "target": "output"
    }
    return(example_3)
# -----------------------------------------------------------
