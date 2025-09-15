#append()
my_list = [1, 2, 3]
print("Original List:", my_list)
my_list.append(4)
print("After append(4):", my_list)
#clear()
my_list2 = [10, 20, 30]
print("Original List:", my_list2)
my_list2.clear()
print("After clear():", my_list2)
#copy()
my_list3 = ["apple", "banana", "cherry"]
copy_list = my_list3.copy()
print("Original List:", my_list3)
print("Copy of List:", copy_list)
#count()
my_list4 = [1, 2, 2, 3, 2, 4]
print("List:", my_list4)
print("Count of 2:", my_list4.count(2))
#extend()
my_list5 = ["red", "blue"]
extra_colors = ["green", "yellow"]
print("Original List:", my_list5)
my_list5.extend(extra_colors)
print("After extend(extra_colors):", my_list5)
#index()
my_list6 = ["cat", "dog", "parrot", "dog"]
print("List:", my_list6)
print("Index of 'dog':", my_list6.index("dog"))
#insert()
my_list7 = [1, 2, 3]
print("Original List:", my_list7)
my_list7.insert(1, 99)
print("After insert(1, 99):", my_list7)
#pop()
my_list8 = ["a", "b", "c", "d"]
print("Original List:", my_list8)
removed_item = my_list8.pop(2)
print("Removed Item:", removed_item)
print("After pop(2):", my_list8)
#remove()
my_list9 = [10, 20, 30, 20, 40]
print("Original List:", my_list9)
my_list9.remove(20)
print("After remove(20):", my_list9)
#reverse()
my_list10 = [1, 2, 3, 4, 5]
print("Original List:", my_list10)
my_list10.reverse()
print("After reverse():", my_list10)
#sort()
my_list11 = [5, 3, 8, 1, 4]
print("Original List:", my_list11)
my_list11.sort()
print("After sort():", my_list11)

