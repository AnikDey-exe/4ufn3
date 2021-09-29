import csv

dataset = []
dataset2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset.append(row)

with open("bright_stars2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset2.append(row)

headers = dataset[0]
data = dataset[1:]

headers2 = dataset2[0]
data2 = dataset2[1:]

headers3 = headers + headers2
star_data = []
for index, data_row in enumerate(data):
    star_data.append(data[index] + data2[index])

with open("starfinal.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

# dataset = dataset[dataset.notna()]

# headers = dataset[0]

# star_data = dataset[1:]

# for dp in star_data:
#     for i in dp[3]:
#         i = i*2
        
#     dp[2] = dp[2]*float(0.000954588)

# for dp in star_data:
#     dp[3] = dp[3]*float(0.102763)

# radius = dataset['Radius']

# for i in radius:
#     i = i*0.102763
#     radius.append(i)

# mass = dataset['Mass']

# for i in mass:
#     i = i*0.000954588
#     mass.append(i)

# with open('stardata2.csv', 'a+') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     # writer.writerow(mass)
#     # writer.writerow(radius)
#     writer.writerows(star_data)