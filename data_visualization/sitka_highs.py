import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Get dates and high temps from file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

# Plot data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()