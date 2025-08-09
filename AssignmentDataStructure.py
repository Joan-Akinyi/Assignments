my_list =[]
print("1 - Empty list:", my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print ("2 - After Appending:", my_list)

my_list.insert(1, 15)
print("3 - After inserting 15:", my_list)

my_list.extend([50, 60, 70])
print ("4 - After extending:", my_list)

my_list.pop()
print("5 - After removing last element:", my_list)

my_list.sort()
print("6 - After Sorting:", my_list)

index_of_30 = my_list.index(30)
print ("7 - Index of value 30 =", index_of_30)
