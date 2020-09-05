pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

def replace_commas(name, *args, **kwargs):
  b = name.replace(',', ' ')
  a = b.split()
  return a

dict_ingridients = {}

food = globals()

names = ['pasta', 'apple_pie', 'ratatouille', 'chocolate_cake', 'omelette']

for i in names:
  key_value = food.get(i)
  get_val = replace_commas(name = key_value)
  for l in names:
    dict_ingridients[l] = get_val

print(dict_ingridients)
