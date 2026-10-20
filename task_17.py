import copy

def merge_dicts(dict_a, dict_b):
    
    for key in dict_b:
        value_b = dict_b[key]

        if key not in dict_a:
            dict_a[key] = copy.deepcopy(value_b)
            continue

        value_a = dict_a[key]

        if isinstance(value_a, dict) and isinstance(value_b, dict):
            merge_dicts(value_a, value_b)
        elif isinstance(value_a, list) and isinstance(value_b, list):
            for item in value_b:
                if item not in value_a:
                    value_a.append(copy.deepcopy(item))
        elif isinstance(value_a, set) and isinstance(value_b, set):
            value_a.update(value_b)
        elif isinstance(value_a, tuple) and isinstance(value_b, tuple):
            new_tuple = value_a
            for item in value_b:
                if item not in new_tuple:
                    new_tuple += (item,)
            dict_a[key] = new_tuple
        else:
            dict_a[key] = copy.deepcopy(value_b)

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(dict_a, dict_b)
print(f"пример из задания: {dict_a}")

dict_c = {"list": [1, 2], "set": {1, 2}, "tuple": (1, 2), "deep": {"x": {"y": [1]}}}
dict_d = {"list": [2, 3], "set": {2, 3}, "tuple": (2, 3), "deep": {"x": {"y": [2], "z": 5}}}
merge_dicts(dict_c, dict_d)
print(f"со вложенными коллекциями: {dict_c}")
