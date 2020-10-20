import datetime
import first_day_after_holiday

def test():
    target = datetime.date(2020, 5, 7)
    output = first_day_after_holiday.first_day_after_holiday(today=target, holiday_duration=4)
    if output == True:
        print('Success!')
    else:
        print('Failed')


if __name__ == "__main__":
    test()