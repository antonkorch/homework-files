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

with open ('recipes.txt') as f:
    lines = f.readlines()

next_idx = 0
cook_book = {}
while next_idx < len(lines):
    recipe, next_idx = read_recipe(lines, next_idx)
    cook_book.update(recipe)

pprint(cook_book)