import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000) or quantity > (max_num - min_num + 1):
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort()
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)