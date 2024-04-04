import matplotlib.pyplot as plt
import csv
from pathlib import Path
from datetime import datetime

path = Path('sitka_weather_2021_simple.csv')
lines =path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates = []
highs = []
lows = []
for row in reader:
    try:
        high = int(row[4])
        date = datetime.strptime(row[2], '%Y-%m-%d')
        low = int(row[5])
    except ValueError:
        print(f'missing data for{date}')
    else:
        highs.append(high)
        dates.append(date)
        lows.append(low)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, color= 'red')
ax.plot(dates, lows, color= 'blue')

ax.set_title('Daily High and low Temprature, 2021', fontsize= 24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temprature(F)', fontsize=16)
ax.tick_params(labelsize = 16)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.5)
fig.autofmt_xdate()

plt.show()