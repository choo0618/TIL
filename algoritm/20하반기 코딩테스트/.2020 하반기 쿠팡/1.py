from datetime import datetime, timedelta

Map = [datetime(2020,1,1,0,0,0)]*3
Time1 = datetime(2020,2,28,23,42,42)
print(Time1)
Time1 += timedelta(days=1)
print(Time1)
