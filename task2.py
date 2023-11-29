from pprint import pprint

def read_recipe(lines, start_idx):
    recipe = {}
    name = lines[start_idx].strip()
    ing_quantity = int(lines[start_idx+1].strip())
    ing_list = []

    for i in range(ing_quantity):
        ing = lines[start_idx+2+i].strip().split(' | ')
        ingredients = {}
        ingredients["ingredient_name"]=ing[0]
        ingredients["quantity"]=ing[1]
        ingredients["measure"]=ing[2]
        ing_list.append(ingredients)

    recipe[name] = ing_list
    next_idx = start_idx + 3 + ing_quantity

    return recipe, next_idx

def get_shop_list_by_dishes(dishes, person_count):
    shoplist = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing["ingredient_name"] not in shoplist:
                    shoplist[ing["ingredient_name"]] = {"measure": ing["measure"], 
                                                        "quantity": int(ing["quantity"])*person_count}
                else:
                    shoplist[ing["ingredient_name"]]["quantity"] += int(ing["quantity"])*person_count
        


    return shoplist

with open ('recipes.txt') as f:
    lines = f.readlines()

next_idx = 0
cook_book = {}
while next_idx < len(lines):
    recipe, next_idx = read_recipe(lines, next_idx)
    cook_book.update(recipe)

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))