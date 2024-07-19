import re

def generator_numbers(text):
    return map(lambda x:float(x),re.findall(r"\b\d+\.\d+\b", text))

def sum_profit(text, func):
    numbers = func(text)
    sum = 0
    for number in numbers:
        sum+=number
    return sum


text = """
Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів.
"""
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
