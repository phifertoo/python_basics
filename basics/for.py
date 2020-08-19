for i in range(3):
    print(i)

# start at 5, end at 10, inccrement by 2
for i in range(5,10,2):
    if i == 7:
        continue
    print(i)

total = 0
for num in range(101):
    total = total + num
print(total)

#________________________________________________________________________________________________________

supplies = ['pens', 'staplers', 'binders']
for i in range(len(supplies)):
    print(supplies[i] + ' has an index of ' + str(i))