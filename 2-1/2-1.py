def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish = line.strip().lower()
            cook_book[dish] = []
            quantity = int(f.readline())
            composition = []
            for i in range(0, quantity):
                composition.append(f.readline().strip('\n'))
            ingridients = []
            for i, comp in enumerate(composition):
                ingridients.append(comp.split('|'))
                cook_book[dish].append({'ingridient_name': ingridients[i][0], 'quantity': int(ingridients[i][1]),
                                        'measure': ingridients[i][2]})
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()