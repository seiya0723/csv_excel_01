import csv

data    = []
for i in range(10):
    row = []

    for j in range(10):
        row.append(j)

    data.append(row)

print(data)


#書き込み
with open("test.csv", "w") as f:
    writer  = csv.writer(f)

    for row in data:
        writer.writerow(row)


#読み込み
with open("test.csv") as f:

    #csvを使わないと、こうなる。
    """
    read_data   = f.read()
    print(read_data)
    """

    #csvを使うとこうなる。
    read_data   = csv.reader(f)
    for row in read_data:
        print(row)






    







