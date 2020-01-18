"""Extract datetimes from log entries and calculate the time
   between the first and last shutdown events"""
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
logfile = os.path.join("/tmp", "log")
urllib.request.urlretrieve("http://bit.ly/2AKSIbf", logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line):
    """TODO 1:
       Given a log line extract its timestamp and convert to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)"""
    log_list = line.split()
    ts = log_list[1]
    dt_from_ts = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S")

    return dt_from_ts


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object."""
    log_array = []
    for line in loglines:
        if "Shutdown" in line:
            log_array.append(line.split())
    first_ts = log_array[0][1]
    last_ts = log_array[-1][1]
    first_dt_from_ts = datetime.strptime(first_ts, "%Y-%m-%dT%H:%M:%S")
    last_dt_from_ts = datetime.strptime(last_ts, "%Y-%m-%dT%H:%M:%S")
    time_diff = last_dt_from_ts - first_dt_from_ts
    return time_diff
