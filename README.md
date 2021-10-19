# micropython-wifi
Scripts to enable WiFi in Micropython with boot.py

## timezone.py - Local Timezone in MicroPython
If you update the time on your device over WiFi using the Network Time Protocol (NTP), the `time.localtime()` command will give you [Coordinated Universal Time (UTC)](https://www.timeanddate.com/time/aboututc.html). This is usually the best standard to use in your projects to avoid switching back and forth between your own Standard Time and Daylight Savings Time, but sometimes you really need to use your own local time.

The `timezone.py` [MicroPython](https://micropython.org/) module converts UTC to [Central Standard Time (CST)](https://www.timeanddate.com/time/zones/cdt) or [Central Daylight Time (CDT)](https://www.timeanddate.com/time/zones/cdt), but you can edit the script to enter your own UTC Offset numbers.

```python
import ntptime
ntptime.host = 'time.cloudflare.com'
ntptime.settime() 

import time
from timezone import tz
time.localtime(tz())
```

My Thanks to [Peter Hinch](https://github.com/peterhinch) for providing this code in a [thread](https://forum.micropython.org/viewtopic.php?t=3675#p28989) on the MicroPython Forum.
