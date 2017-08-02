#!/usr/bin/python
######################################################################

#       Filename: test_mars.py

#       Author: Stefan Luedtke

######################################################################

from ecmwf_mars import mars
import pytest

######################################################################


# Check whether the creating the object succeeds
def test_read_example_1():
    temp = mars.mars_request("./ecmwf_mars/tests/example_data/example_1.txt")
    assert isinstance(temp, mars.mars_request), 'Wrong data type'


@pytest.fixture(scope="session")
def mars_example_1():
    temp = mars.mars_request("./ecmwf_mars/tests/example_data/example_1.txt")
    return(temp)


# Compare whether the parsed mars request is identical to the ECMWF output
# (copied from the website)
def test_read_mars_example_1(example_1, mars_example_1):
    assert mars_example_1.request == example_1


# Compare the number of parsed parameters
def test_parse_para_mars_example_1(example_1, mars_example_1):
    assert len(mars_example_1.para_list) == 1
    assert mars_example_1.para_list == ['168.128']


# Compare the number of parsed years
def test_parse_year_mars_example_1(example_1, mars_example_1):
    assert len(mars_example_1.year_list) == 1
    assert mars_example_1.year_list == [1979]


# Compare the number of parsed dates
def test_parse_dates_mars_example_1(example_1, mars_example_1):
    assert len(mars_example_1.date_list) == 31
    assert mars_example_1.date_list[0] == '1979-01-01'
    assert mars_example_1.date_list[-1] == '1979-01-31'
# -----------------------------------------------------------


# Check whether the creating the object succeeds
def test_read_example_2():
    temp = mars.mars_request("./ecmwf_mars/tests/example_data/example_2.txt")
    assert isinstance(temp, mars.mars_request), 'Wrong data type'


@pytest.fixture(scope="session")
def mars_example_2():
    temp = mars.mars_request("./ecmwf_mars/tests/example_data/example_2.txt")
    return(temp)


# Compare whether the parsed mars request is identical to the ECMWF output
# (copied from the website)
def test_read_mars_example_2(example_2, mars_example_2):
    assert mars_example_2.request == example_2


# Compare the number of parsed parameters
def test_parse_para_mars_example_2(example_2, mars_example_2):
    assert len(mars_example_2.para_list) == 2
    assert mars_example_2.para_list == ['63.162', '168.128']


# Compare the number of parsed years
def test_parse_year_mars_example_2(example_2, mars_example_2):
    assert len(mars_example_2.year_list) == 1
    assert mars_example_2.year_list == [1979]


# Compare the number of parsed dates
def test_parse_dates_mars_example_2(example_2, mars_example_2):
    assert len(mars_example_2.date_list) == 59
    assert mars_example_2.date_list[0] == '1979-01-01'
    assert mars_example_2.date_list[-1] == '1979-02-28'
# -----------------------------------------------------------


# Check whether the creating the object succeeds
def test_read_example_3():
    temp = mars.mars_request("./ecmwf_mars/tests/example_data/example_3.txt")
    assert isinstance(temp, mars.mars_request), 'Wrong data type'


@pytest.fixture(scope="session")
def mars_example_3():
    temp = mars.mars_request("./ecmwf_mars/tests/example_data/example_3.txt")
    return(temp)


# Compare whether the parsed mars request is identical to the ECMWF output
# (copied from the website)
def test_read_mars_example_3(example_3, mars_example_3):
    assert mars_example_3.request == example_3


# Compare the number of parsed parameters
def test_parse_para_mars_example_3(example_3, mars_example_3):
    assert len(mars_example_3.para_list) == 2
    assert mars_example_3.para_list == ['63.162', '168.128']


# Compare the number of parsed years
def test_parse_year_mars_example_3(example_3, mars_example_3):
    assert len(mars_example_3.year_list) == 2
    assert mars_example_3.year_list == [1979, 1980]


# Compare the number of parsed dates
def test_parse_dates_mars_example_3(example_3, mars_example_3):
    assert len(mars_example_3.date_list) == 731
    assert mars_example_3.date_list[0] == '1979-01-01'
    assert mars_example_3.date_list[-1] == '1980-12-31'
