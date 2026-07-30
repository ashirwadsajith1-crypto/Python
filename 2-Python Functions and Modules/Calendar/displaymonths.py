import calendar
def print_month_names():
    for month_num in range(1, 13):
        print(calendar.month_name[month_num])
print_month_names()