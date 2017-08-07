# ECMWF_MARS

A python library on top of ECMWF-API to download ERA-Interim data via python. 

While the ECMWF-API provides the client library to access the server,
the ECMWF-MARS library tries to make the download as easy as possible. 
Assuming everything is setup correctly, an example looks like that:

1. Select the data from the web interface and save the **mars request only** as
   a text file.
2. create a python script with the following content.

```python
from  ecmwf_mars import mars

example = mars.mars_request("path/to/filename")

example.fetch_data()

```

This will split the list of parameters and the given time period into single
years and download each slice separately in the current working directory as
files following the naming ` data_{year]_{parameter_code}.[grib, nc] `

# Requirements

The package requires the ECMWF-API and the python modules `datetime` and `re`.
The first one comes with the installation of this package. The second on (re)
has to be installed manually via pip `pip install re`.

In addition, the library from ECMWF is required to download the data.

All libraries are loaded on demand. 

## The ECMWF API

The eccmwfapi has to be installed prior to running the script. See the
following
[link](https://software.ecmwf.int/wiki/display/WEBAPI/Accessing+ECMWF+data+servers+in+batch#AccessingECMWFdataserversinbatch-python)
for help and instructions.


On Unix/Linux
```
pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz --user
```

On Windows
```
pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz
```

If you cannot run the sudo or pip commands, ask your sysdamin.

The file .ecmwfapirc contains the access key and has to be placed in the home
directory of your system.  For windows this should be
'C:/User/'username'/.ecmwfapirc'. For Linux this should be
'/home/'username'/.ecmwfapirc'.

The file looks like that and the keys can be found on the webpage
```
{
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "*************************",
    "email" : "***********************"
}
```

# Installation

The installation via pip works like that:

```
pip install git+ssh://git@github.com/sluedtke/ecmwf_mars.git
```
