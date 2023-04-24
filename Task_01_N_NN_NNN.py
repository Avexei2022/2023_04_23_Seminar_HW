from get_input_value import get_number

def get_result(number):
    num_list = []
    num_to_list = number
    sum_result = 0
    for i in range(3):
        num_list.append(num_to_list)
        sum_result += num_to_list
        num_to_list = int(str(num_to_list) + str(number))
    return num_list, sum_result


def print_result(number, num_list, sum_result):
    print(f"N = {number}: ", end='')
    print(*num_list, sep=" + ", end=" = ")
    print(sum_result)

num_min, num_max = 1, 1000000
message = f"Введите натуральное число N (от {num_min} до {num_max}):"
mes_false = "Условия ввода не выполнены."
number = get_number(message, num_min, num_max, mes_false)
num_list, sum_result = get_result(number)
print_result(number, num_list, sum_result)
