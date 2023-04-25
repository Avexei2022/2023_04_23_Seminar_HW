from random import randint
from get_input_value import get_number


def number_input() -> int:
    num_min, num_max = 100, 999
    message = f"Введите натуральное число N (от {num_min} до {num_max}):"
    mes_false = "Условия ввода не выполнены."
    number = get_number(message, num_min, num_max, mes_false)
    return number


def search_sequance(num_list, num_for_check):
    num_for_check_list = list(map(lambda x: int(x), list(str(num_for_check))))
    for i in range(0, 13):
        if num_list[i: i + 3] == num_for_check_list:
            return 'да'
    return "нет"


num_list = [randint(0, 9) for i in range(15)]
print(num_list)
num_for_check = number_input()
result = search_sequance(num_list, num_for_check)
print(f"{num_list} - {num_for_check} -> {result}")
