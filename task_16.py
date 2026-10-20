def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            inner = lst[i]
            flatten_list(inner)
            lst[i:i + 1] = inner
            i += len(inner)
        else:
            i += 1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(f"список до: {list_a}")
flatten_list(list_a)
print(f"список после: {list_a}")
