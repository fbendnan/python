def validate_ingredients(ingredients: str) -> str:
    ingredients_list = ingredients.split(" ")
    for ingredient in ingredients_list:
        if ingredient != 'fire' and ingredient != 'water' and\
           ingredient != 'earth' and ingredient != 'air':
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
