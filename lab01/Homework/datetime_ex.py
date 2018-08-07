import datetime
now = datetime.time.now()
print ("{3}:{4}:{5} {2}-{1}-{0}".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
