#!/usr/bin/python
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
        return new_list
    my_list = [1, 2, 3, 4, 5]

    new_list = delete_at(my_list, 2)
    print(new_list)

    new_list_negative = delete_at(my_list, -1)
    print(new_list_negative)

    new_list_out_of_range = delete_at(my_list, 10)
    print(new_list_out_of_range)
