#!/usr/bin/python
######################################################################

#       Filename: mars.py

#       Author: Stefan Luedtke

######################################################################

from ecmwfapi import ECMWFDataServer
from datetime import datetime, timedelta
import re

######################################################################


def identify_days(year_string, date_list):
    """
    The function takes a single integer number (4 digits) and returns all
    items of a list that have this number at the very beginning.

    :year_string: a string that is equivalent to a four digit integer
    :date_list: a list of dates or anything else, but we are working on
                dates so anything does not make sense
    :returns: TODO

    """
    r = re.compile("^{}-".format(year_string))
    dates = list(filter(r.match, date_list))
    return(dates)
# -----------------------------------------------------------


class mars_request(object):
    """
    A class that holds all information required for the mars request.

    """
    # -----------------------------------------------------------
    def read_mars_file(self):
        """
        Reads the plain text file (mars request) and translates this into a
        dictionary.

        :returns: dictionary with the parameters of the mars request.


        """
        # create empty dictionary
        mars_dict = {}
        # open file
        with open(self.mars_file_name) as f:
            # skip first line
            next(f)
            for line in f:
                # read each line as key value
                (key, val) = line.split("=")
                # get rid of unnecessary characters
                val = val.replace('"', '').replace('\n', '').replace(',', '')
                mars_dict[key] = val
        return(mars_dict)
    # -----------------------------------------------------------

    def separate_para(self):
        """
        Take the 'param' key and separates that in a list single parameters.

        :mars_dict:
        :returns:

        """
        self.para_list = self.request['param'].split('/')
        return(self)
    # -----------------------------------------------------------

    def make_date_list(self):
        """
        Take the 'date' key and separates that in a list of strings that
        describe an entire year for the MARS interface

        :mars_request:
        :returns: a list with 2 items: the mars request dictionary with an
            empty parameter slot and a list with the parameters.

        """
        # split the range into start and end
        dates = self.request['date'].split('/to/')
        # create start from the first item on the list
        start = datetime.strptime(dates[0], '%Y-%m-%d').date()
        # create end from the second/last item on the list
        end = datetime.strptime(dates[-1], '%Y-%m-%d').date()
        # create the full date list as strings
        day_count = (end - start).days
        date_list = [start + timedelta(days=n) for n in range(day_count + 1)]
        date_list = [datetime.strftime(day, format="%Y-%m-%d") for day in
                     date_list]
        self.date_list = date_list
        # get only the years and create list
        year_list = list(range(start.year, end.year + 1))
        self.year_list = list(map(str, year_list))
        return(self)
    # -----------------------------------------------------------

    def __init__(self, mars_file):
        """
        A function that read the __plain__ mars request from ECMWF into a
        python dictionary.  The first line will be skipped.

        """
        # put the filename into a slot
        self.mars_file_name = mars_file
        # assign properties to the created object
        self.request = self.read_mars_file()
        # create the slot with the separated parameters
        self.separate_para()
        # create the slot with dates and years
        self.make_date_list()
    # -----------------------------------------------------------

    def update_request(self, year, para):
        """
        Updates the mars request slot with a subset of the required dates (for
        one year) and a single parameter and the file name.

        :year: the year we want to use as a filter
        :para: the parameter we want to use for the request
        :returns: an update of the mars request slot

        """
        # select the dates for the given year join them to one string with '/'
        dates = '/'.join(identify_days(year, self.date_list))
        # update the request slot
        self.request['date'] = dates
        self.request['param'] = para
        # ------------------------------------------------------
        #  concatenate arguments to string and fill the filename slot in the
        #  request dictionary
        try:
            if self.request['format'] == 'netcdf':
                file_name = './data_' + str(year) + '_' + str(para) + '.nc'
            else:
                file_name = './data_' + str(year) + '_' + str(para) + '.grib'
        except KeyError:
            file_name = './data_' + str(year) + '_' + str(para) + '.grib'
        # ------------------------------------------------------
        self.request['target'] = file_name
        return(self)

    # -----------------------------------------------------------
    def fetch_data(self):
        """
        Calling this method, will iterate over the 'para_list' slot and the
        'year_list' slot, both created at the very moment the object is
        initiated and download the data.

        :returns:  nothing yet

        """
        # init the server object
        server = ECMWFDataServer()

        # iterate of the parameter list
        for para in self.para_list:
            # iterate of the list of years
            for year in self.year_list:
                # update the dictionary
                self.update_request(year, para)
                # query the ECMWF api
                server.retrieve(self.request)
