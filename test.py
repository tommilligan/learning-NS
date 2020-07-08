import json
import os
from datetime import datetime, timedelta

from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key=os.environ["ALPHA_VANTAGE_KEY"])

# Get json object with the intraday data and another with  the call's metadata
# get the last 100 data points
data, meta_data = ts.get_daily("GOOGL", outputsize="compact")

# Do stuff first : open the file
with open("GOOGL_daily.json", "w") as file_handle:
    # doing some instructions
    json.dump(data, file_handle)
# <- when we leave the with block, close the file


# The time now
today = datetime.utcnow()
for days_ago in range(1, 8):
    day = today - timedelta(days=days_ago)
    day_string = day.strftime("%Y-%m-%d")
    print(day_string)

    try:
        day_data = data[day_string]
    except KeyError:
        # jump straight to the next loop day
        continue

    print(day_data)
