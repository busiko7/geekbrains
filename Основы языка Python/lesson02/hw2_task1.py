# 1. Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#     Примечание. Списки создайте вручную, например так:

my_list_1 = [22, 5, 8, 2, 112, 12, 4, 209, 77]
my_list_2 = [22, 7, 112, 3, 155, 209]

print(my_list_1)
print(my_list_2)

for item in my_list_2:
    if item in my_list_1:
        my_list_1.remove(item)
print(my_list_1)
