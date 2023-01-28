import os


def read_cook_book(file_name):
    """ Cоздание словаря из файла с рецептами """
    result = {}
    with open(file_name, 'rt', encoding='utf8') as f:
        result = {}
        for line in f:
            dish_name = line.strip()
            ingr_count = int(f.readline().strip())
            result[dish_name] = []
            for _ in range(ingr_count):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                result[dish_name].append({'ingredient_name': ingredient_name,
                                          'quantity': int(quantity),
                                          'measure': measure})
            f.readline()
    return result


def get_shop_list_by_dishes(dishes, person_count):
    """ Cоздание словаря ингридиентов для количества человек """
    result = {}
    for key, val in cook_book.items():
        if key in dishes:
            for el in cook_book[key]:
                if el['ingredient_name'] not in result:
                    result[el['ingredient_name']] = {'measure': el['measure'],
                                                     'quantity': el['quantity'] * person_count}
                else:
                    result[el['ingredient_name']]['quantity'] += el['quantity'] * person_count
    return result


cook_book = read_cook_book('cook_book.txt')
shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list_by_dishes)
