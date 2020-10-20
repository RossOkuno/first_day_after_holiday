import datetime
from datetime import timedelta

import jpholiday

def first_day_after_holiday(today, holiday_duration):
  count = 0
  for days_to_subtract in range(1, holiday_duration+1):
    day = today - timedelta(days=days_to_subtract)
    if day.weekday() > 4 or jpholiday.is_holiday(day) == True:
      count+=1
    else:
      return False

  return True


if __name__ == "__main__":
    pass