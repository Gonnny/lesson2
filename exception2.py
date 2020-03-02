"""
Домашнее задание №1
Исключения: приведение типов
* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало

def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

"""

def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
        get_summ = num_one + num_two
        return(get_summ)
    except ValueError:
        return("Введён не тот тип данных")

if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
    