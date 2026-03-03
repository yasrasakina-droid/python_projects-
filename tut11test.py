list1=[12,13,14,67,4,6,8,9,"yasra",34.6,45.7]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)