#!/usr/bin/python
######################################################################

#       Filename: test_mars.py

#       Author: Stefan Luedtke

######################################################################

from ecmwf_mars import mars
import re
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
    assert mars_example_1.year_list == ['1979']


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
    assert mars_example_2.year_list == ['1979']


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
    assert mars_example_3.year_list == ['1979', '1980']


# Compare the number of parsed dates
def test_parse_dates_mars_example_3(example_3, mars_example_3):
    assert len(mars_example_3.date_list) == 731
    assert mars_example_3.date_list[0] == '1979-01-01'
    assert mars_example_3.date_list[-1] == '1980-12-31'
# -----------------------------------------------------------


def test_identify_days():
    a = ["1990-01-01", "1990-01-02", "1991-01-01"]
    temp = mars.identify_days('1990', a)
    assert temp == ["1990-01-01", "1990-01-02"]
    # --------------------------------
    temp = mars.identify_days('1991', a)
    assert temp == ["1991-01-01"]
    # --------------------------------
    temp = mars.identify_days('1992', a)
    assert temp == []
    # --------------------------------
    temp = mars.identify_days('199', a)
    assert temp == []
    # --------------------------------
    temp = mars.identify_days('990', a)
    assert temp == []
    # --------------------------------
    temp = mars.identify_days('991', a)
    assert temp == []
# -----------------------------------------------------------


# check whether the update procedure succeeds
def test_update_request_example_1(mars_example_1):
    mars_example_1.update_request('1979', '168.128')
    assert mars_example_1.request['param'] == '168.128'
    # --------------------------------
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_1.date_list))
    temp_2 = list(filter(r.findall, mars_example_1.request['date'].split('/')))
    assert temp_1 == temp_2
    # check the filname for output
    assert mars_example_1.request['target'] == './data_1979_168.128.grib'


# it should fail with a different year and parameter than in the original
# dictionary
@pytest.mark.xfail
def test_update_request_example_1_xfail_a(mars_example_1):
    mars_example_1.update_request('1990', '172.128')
    assert mars_example_1.request['param'] == '168.128'


# it should fail with a different year and parameter than in the original
# dictionary
@pytest.mark.xfail
def test_update_request_example_1_xfail_b(mars_example_1):
    mars_example_1.update_request('1990', '172.128')
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_1.date_list))
    temp_2 = list(filter(r.findall, mars_example_1.request['date'].split('/')))
    assert temp_1 == temp_2
# -----------------------------------------------------------


# check whether the update procedure succeeds
def test_update_request_example_2(mars_example_2):
    mars_example_2.update_request('1979', '168.128')
    assert mars_example_2.request['param'] == '168.128'
    # --------------------------------
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_2.date_list))
    temp_2 = list(filter(r.findall, mars_example_2.request['date'].split('/')))
    assert temp_1 == temp_2
    # check the filname for output
    assert mars_example_2.request['target'] == './data_1979_168.128.grib'


# it should fail with a different year and parameter than in the original
# dictionary
@pytest.mark.xfail
def test_update_request_example_2_xfail_a(mars_example_2):
    mars_example_2.update_request('1990', '172.128')
    assert mars_example_2.request['param'] == '168.128'


# it should fail with a different year and parameter than in the original
# dictionary
@pytest.mark.xfail
def test_update_request_example_2_xfail_b(mars_example_2):
    mars_example_2.update_request('1990', '172.128')
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_2.date_list))
    temp_2 = list(filter(r.findall, mars_example_2.request['date'].split('/')))
    assert temp_1 == temp_2
# -----------------------------------------------------------


# check whether the update procedure succeeds 
def test_update_request_example_3_a(mars_example_3):
    mars_example_3.update_request('1979', '168.128')
    assert mars_example_3.request['param'] == '168.128'
    # --------------------------------
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_3.date_list))
    temp_2 = list(filter(r.findall, mars_example_3.request['date'].split('/')))
    assert temp_1 == temp_2
    # check the filname for output
    assert mars_example_3.request['target'] == './data_1979_168.128.grib'


# check whether the update procedure succeeds
def test_update_request_example_3_b(mars_example_3):
    mars_example_3.update_request('1980', '168.128')
    assert mars_example_3.request['param'] == '168.128'
    # --------------------------------
    r = re.compile("{}".format('1980'))
    temp_1 = list(filter(r.findall, mars_example_3.date_list))
    temp_2 = list(filter(r.findall, mars_example_3.request['date'].split('/')))
    assert temp_1 == temp_2
    # check the filname for output
    assert mars_example_3.request['target'] == './data_1980_168.128.grib'


# check whether the update procedure succeeds
def test_update_request_example_3_c(mars_example_3):
    mars_example_3.request['format'] = 'netcdf'
    mars_example_3.update_request('1979', '63.162')
    assert mars_example_3.request['param'] == '63.162'
    # --------------------------------
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_3.date_list))
    temp_2 = list(filter(r.findall, mars_example_3.request['date'].split('/')))
    assert temp_1 == temp_2
    # check the filname for output
    assert mars_example_3.request['target'] == './data_1979_63.162.nc'


# check whether the update procedure succeeds
def test_update_request_example_3_d(mars_example_3):
    mars_example_3.request['format'] = 'netcdf'
    mars_example_3.update_request('1980', '63.162')
    assert mars_example_3.request['param'] == '63.162'
    # --------------------------------
    r = re.compile("{}".format('1980'))
    temp_1 = list(filter(r.findall, mars_example_3.date_list))
    temp_2 = list(filter(r.findall, mars_example_3.request['date'].split('/')))
    assert temp_1 == temp_2
    # check the filname for output
    mars_example_3.request['format'] = 'netcdf'
    assert mars_example_3.request['target'] == './data_1980_63.162.nc'


# it should fail with a different year and parameter than in the original
# dictionary
@pytest.mark.xfail
def test_update_request_example_3_xfail_a(mars_example_3):
    mars_example_3.update_request('1990', '172.128')
    assert mars_example_3.request['param'] == '168.128'


# it should fail with a different year and parameter than in the original
# dictionary
@pytest.mark.xfail
def test_update_request_example_3_xfail_b(mars_example_3):
    mars_example_3.update_request('1990', '172.128')
    r = re.compile("{}".format('1979'))
    temp_1 = list(filter(r.findall, mars_example_3.date_list))
    temp_2 = list(filter(r.findall, mars_example_3.request['date'].split('/')))
    assert temp_1 == temp_2
# -----------------------------------------------------------
