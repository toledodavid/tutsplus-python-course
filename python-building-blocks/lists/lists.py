list = [2, 4, 6, 8, 10]
print(list)

print(list[4]) #10

#print(list[5]) #IndexError: list index out of range

print(len(list)) #5

print(list[0:2]) #[2, 4]

print(list[:3]) #[2, 4, 6]

print(list[:]) #[2, 4, 6, 8, 10]

list2 = [12, 14, 16, 18, 20];

list3 = list + list2

print(list3) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


list2.append(22)

print(list2) #[12, 14, 16, 18, 20, 22]

list4 = [1, 2, "3", [4, 5, 6]]

print(list4[3][2]) #6

list2.remove(22) # Removes the value from the list

print(list2) #[12, 14, 16, 18, 20]

del(list2[0]) # Removes the value in the index 0

print(list2) #[14, 16, 18, 20]