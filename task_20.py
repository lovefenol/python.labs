def unique_elements(nested_list, result=None):
    if result is None:
        result = []

    for element in nested_list:
        if isinstance(element, list):
            unique_elements(element, result)
        else:
            if element not in result:
                result.append(element)
    return result


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(f"исходный список: {list_a}")
print(f"уникальные элементы: {unique_elements(list_a)}")
