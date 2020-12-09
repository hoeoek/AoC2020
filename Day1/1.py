import csv

file = "input.txt"
number_list = []

with open(file) as csvfile:
    q = csv.reader(csvfile)
    for row in q:
        number_list.append(int(row[0]))

for i in number_list:
    for j in number_list:
        for k in number_list:
            res = i + j + k
            if res == 2020:
                print("here they are: {} + {} + {} = {}".format(i,j,k,i+j+k))
                print("{} * {} * {} = {}".format(i,j,k,i*j*k))
                break
