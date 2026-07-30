Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Python Collections / Non-primitive datatypes
#--------------------------------------------
#List / Tuple / Set / Dictionary

#DICTIONARY
#----------
# Dictionary is enclosed with {key:value} paired items
# Dictionary contains ordered collection of data items
# Dictionary is not indexed
# Dictionary don't allow duplicate values
# Support heterogenous data items

car = {} #create an empty dictionary
type(car)
<class 'dict'>
car['brand'] = 'VW'
car['model'] = 'polo'
car['price'] = '1500000'
car
{'brand': 'VW', 'model': 'polo', 'price': '1500000'}
car['brand']
'VW'
car['model']
'polo'
car.keys()
dict_keys(['brand', 'model', 'price'])
car.values()
dict_values(['VW', 'polo', '1500000'])
car.items()
dict_items([('brand', 'VW'), ('model', 'polo'), ('price', '1500000')])
car.get('model')
'polo'
car.pop('price')
'1500000'
car
{'brand': 'VW', 'model': 'polo'}
car.popitem()
('model', 'polo')
car
{'brand': 'VW'}
car.setdefault('model','Polo')
'Polo'
car
{'brand': 'VW', 'model': 'Polo'}
car.setdefault('model')
'Polo'
car
{'brand': 'VW', 'model': 'Polo'}
value = car.setdefault('model','Vento')
value
'Polo'
car1 = car.fromkeys(car.keys())
car1
{'brand': None, 'model': None}
car
{'brand': 'VW', 'model': 'Polo'}














