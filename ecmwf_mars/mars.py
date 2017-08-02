#!/usr/bin/python
######################################################################

#       Filename: mars.py

#       Author: Stefan Luedtke

######################################################################

from datetime import datetime, timedelta

######################################################################


class mars_request(object):

    """
    A class that holds all information required for the mars request.
    """
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

    def separate_para(self):
        """
        Take the 'param' key and separates that in a list single parameters
        :mars_dict
        :returns: a list with 2 items:
                  the mars request dictionary with an empty parameter slot and
                  a list with the parameters.
        """
        self.para_list = self.request['param'].split('/')
        return(self)

    def make_date_list(self):
        """
        Take the 'date' key and separates that in a list of strings that
        describe an entire year for the MARS interface
        :mars_request
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
        self.year_list = list(range(start.year, end.year + 1))
        return(self)

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
