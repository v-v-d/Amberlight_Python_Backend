"""
Необходимо написать функцию, которая на вход получает некий список, состоящий из конечных элементов или вложенных
списков, причем вложенность неизвестна и может быть какой угодно.
Например:
[1, 2, [[3, 4], [[[5, 6]]]], 7, [8, 9], [[[10, [11, [12]]]]]]
Функция должна вернуть плоский список, состоящий только из конечных элементов:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""


def uncover_a_list(input_list, output_list=None):
    if output_list is None:
        output_list = []
    for i in input_list:
        uncover_a_list(i, output_list) if type(i) is list else output_list.append(i)
    return output_list


test_list_1 = [1, 2, [[3, 4]], [[[5, 6]]], 7, [8, 9], [[[10, [11, 12]]]]]
test_list_2 = [1, 2, 3]
test_list_3 = [1, [2, 2, 2], 4]
test_list_4 = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
test_list_5 = [-1, [1, [-2], 1], -1]

print(uncover_a_list(test_list_1))
print(uncover_a_list(test_list_2))
print(uncover_a_list(test_list_3))
print(uncover_a_list(test_list_4))
print(uncover_a_list(test_list_5))
