from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    # Extract the IOS Time using the regex from each given line.
    event_time = re.search( r'(\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d(?:\.\d+)?Z?)', line)

    # Fetch the searched Object
    time_obj = event_time.group()

    # Finally return the time object in datetime format
    datetime_format = datetime.fromisoformat(time_obj)
    return datetime_format


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    # Create an empty list to store time stamps
    events = []

    # loop through given logline to find the first and the last even of "Shutdown initiated"
    for logline in loglines:
        # Only if the "Shutdown inititated" exists in the line append it to the events list.
        if SHUTDOWN_EVENT in logline:
            events.append(convert_to_datetime(logline))
    
    # Find the difference in the first and last event.
    time_delta = events[-1] - events[0]

    # total_seconds = time_delta.total_seconds()
    # total_mins = total_seconds / 60
    # total_hours = total_mins / 60
    
    # return f"The time between shutdowns {round(total_mins, 2)} minutes or {total_seconds} in seconds"
    return time_delta
