import os
os.path.join("Users", "Tatiana", "test.txt")
st = open("test.txt", "w")
st.write("Python!")
st.close()

with open("test.txt", "w") as f:
    f.write("привет от Python!")

# убедитесь, что файл от предыдущего примера
with open("test.txt", "r") as f:
    print(f.read())


my_list = list()
with open("test.txt", "r") as f:
    my_list.append(f.read())
print(my_list)

import csv
with open("test.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["один", "два", "три"])
    w.writerow(["четыре", "пять", "шесть"])

# with open("test.csv", "r") as f:
#     print(f.read())

import csv
with open("test.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))


