#pull critical errors out of event logs

import win32evtlog
import time
import datetime
import pywintypes

def write_to_file(filename, message):
    with open(filename, "a") as file:
        file.write(message + "\n")

def check_event_logs():
    server = 'localhost'
    logtype = 'System'
    hand = win32evtlog.OpenEventLog(server, logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    time_last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    event_time_last_week = time.mktime(time_last_week.timetuple())

    #date and time
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H%M")
    filename = f"Error_Log_{timestamp}.txt"

    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events: 
            break

        for event in events:
            pywin_time = event.TimeGenerated
            event_created = datetime.datetime(pywin_time.year, pywin_time.month, pywin_time.day, 
                                              pywin_time.hour, pywin_time.minute, pywin_time.second)
            
            if event_created.timestamp() < event_time_last_week:
                continue  

            #writes to new file or overwrites if one exists
            if event.EventType == win32evtlog.EVENTLOG_ERROR_TYPE:
                message = f"Critical Error Detected on {event_created}: Error in {event.SourceName}: {event.StringInserts}"
                write_to_file(filename, message)

check_event_logs()
