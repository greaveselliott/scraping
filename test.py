import csv

with open("./output.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b", "c"])