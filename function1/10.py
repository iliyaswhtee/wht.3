def g_unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

my_list = list(input("Enter your list: "))
unique_elements = g_unique_elements(my_list)
print("Unique elements:",unique_elements)