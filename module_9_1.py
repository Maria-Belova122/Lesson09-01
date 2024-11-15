# ЗАДАНИЕ ПО ТЕМЕ "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    result = {}
    list_functions = list(functions)
    # Преобразуем список int_list в список чисел
    numbers = list(map(int, int_list))
    for function in list_functions:
        key = function.__name__
        result[key] = function(numbers)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
