from datetime import datetime

time = str(input('enter date in this format >> yyyy-mm-dd  : '))
time_loc = datetime.strptime(time, "%Y-%m-%d")
time_formatted = datetime.strftime(time_loc, "%a - %b - %Y")
print(time_formatted)
