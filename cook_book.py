with open("cook_book.txt", "r", encoding="utf-8") as file:
    cook_book_dict = {}
    cook_book_keys = ["имя ингредиента", "количество", "единица измерения"]
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        dish_ingr_list = []
        for _ in range(counter):
            ingr = file.readline().strip().split("|")
            ing_dict = dict(zip(cook_book_keys, ingr))
            dish_ingr_list.append(ing_dict)
        file.readline()
        cook_book_dict[dish_name] = dish_ingr_list

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book_dict[dish]:
            ing_name = ing["имя ингредиента"]
            if ing_name not in shop_list:
                shop_list[ing_name] = {"количество": int(ing["количество"]) * person_count, "единица измерения": ing["единица измерения"]}
            else:
                shop_list[ing_name]["количество"] += int(ing["количество"]) * person_count
    return shop_list

from pprint import pprint
cook_book_keys
pprint(cook_book_dict)
print()
from pprint import pprint
get_shop_list_by_dishes
pprint(get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 3))