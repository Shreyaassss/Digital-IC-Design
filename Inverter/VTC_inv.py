import csv
import matplotlib.pyplot as plt

filename = 'D:\DIC\inverter_csv.csv'
with open(filename) as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0

    for row in f:
        x=(float(row[1]))
        y=(float(row[2]))
        print(float(row[1]))
        print(float(row[2]))

plt.bar(x,y)
plt.xticks(y)
plt.ylabel('Vout')
plt.title('Vinp')
plt.show()