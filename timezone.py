# Brandon Gant
# Created: 2021-10-13
# Updated: 2021-11-03
#
# Sources:
#   Peter Hinch: https://forum.micropython.org/viewtopic.php?t=3675#p28989
#   https://www.timeanddate.com/time/zones/cst
#
# This script only really works if you have set the time over WiFi using NTP.
# Timezones in North America switch to Daylight Savings Time at 2AM on the Second Sunday in March. 
# They switch to Standard Time at 2AM on the First Sunday in November.
#
# Usage:
#   import time
#   from timezone import tz
#   time.localtime(tz())
#

UTC_Offset_ST  = -6  # CST
UTC_Offset_DST = -5  # CDT

import time
def tz(format='time'):
    t = time.time()
    year = time.localtime(t)[0]
    start = time.mktime((year, 3,(14-(int(5*year/4+1))%7),2,0,0,0,0))  # 2AM the Second Sunday in March
    end   = time.mktime((year,11,( 7-(int(5*year/4+1))%7),2,0,0,0,0))  # 2AM the  First Sunday in November
    if format == 'time':
        return t + (3600 * UTC_Offset_ST) if t < start or t > end else t + (3600 * UTC_Offset_DST)
    elif format == 'bool':
        return False if t < start or t > end else True
    else:
        return None
