import pprint

def parse_recipes(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            if lines[i] == '\n':
                i += 1
                continue
            
            dish_name = lines[i].strip()  # Название блюда
            i += 1
            
            ingredient_count = int(lines[i].strip())  # Количество ингредиентов
            i += 1
            
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = lines[i].strip()
                ingredient_name, quantity, measure = ingredient_line.split(', ')
                
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
                i += 1
            
            cook_book[dish_name] = ingredients
    
    return cook_book

# Используйте функцию, передав путь к вашему файлу recipes.txt
cook_book = parse_recipes('lesson7-files\\recipes.txt')
pprint.pprint(cook_book)