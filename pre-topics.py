# ------------------ Load Modules -> random module -------------- #
from random import seed, randint
# n = int(input())
# fake random int, if seed is the same num, the output is same
seed(40)
print(randint(-50,50))

# ------------------ Tuples -------------- #
bakers_dozen = tuple([12, 1])
print(bakers_dozen)  # (12, 1)

sound = tuple('meow')
print(sound)  # ('m', 'e', 'o', 'w')

# ------------------ Arges -------------- #
print(*"fun") 
print(*[5, 10, 15])

def congratulations(project_manager, tester, *args):
    print('Happy New Year! Take care of yourself and your loved ones!\nFor:')
    print(project_manager, tester, *args, sep="\n")

congratulations('Alice', 'Mike', 'Roman', 'Victoria')

# ------------------ Dictionary -------------- #
new_dict = dict()
cafe_price = dict(
    {'espresso': 2.3},
    americano=2.0,
    latte=2.5,
    pastry='Varies peices'
)
print(cafe_price['latte']) 
# Create
coffees = {'americano', 'latte', 'flatwhite'}
coffee_dict = dict.fromkeys(coffees)
print(coffee_dict)
price = 2.6
coffee_dict = dict.fromkeys(coffees, price)
print(coffee_dict)
coffee_dict['flatwhite'] = 0.9 + coffee_dict['flatwhite']
print(coffee_dict)
ingredient = ['espresso', 'water', 'milk']
coffee_dict = dict.fromkeys(coffees, [])
print(coffee_dict)
coffee_dict['americano'].append(ingredient[0])
print(coffee_dict)
# Add
coffee_dict.update(espresso=['espresso'])
print(coffee_dict)
# Get
print(coffee_dict.get('oat latte', 'no such coffee'))
# Remove
print(coffee_dict.pop('oat latte', 'no such coffee'))
remove_value = coffee_dict.pop('flatwhite')
print(remove_value)
print(coffee_dict)
remove_value = coffee_dict.popitem()
print(remove_value)
# Clean
dict = {'December': 12, 'July': 7}
new_dict = dict
dict = {}
print(new_dict)  # {'December': 12, 'July': 7}

dict = {'December': 12, 'July': 7}
new_dict = dict
dict.clear()
print(new_dict)  # {}

# Operations
month_dict = {'May': 5, 'June': 6, 'July': 7}
for obj in month_dict:
    print(obj)
print(month_dict.keys())
for obj in month_dict.keys():
    print(obj)

for value in month_dict.values():
    print(value)
for obj in month_dict.items():
    print(obj)

word_list = 'win'
word_dict = {}
for word in word_list.split():
    try:
        word_dict[word.lower()] += 1
    except KeyError:
        word_dict[word.lower()] = 1

for key in word_dict:
    print(key, word_dict[key])

# ------------------ File in Python -------------- #
with open('test.txt', 'r') as my_file:
    data = my_file.read()
    print(data)
with open('test.txt', 'r') as my_file:
    data = my_file.readline(3)
    print(data)
with open('test.txt', 'r') as my_file:
    data = my_file.readlines()
    print(data)

with open('test.txt', 'r') as my_file:
    for line in my_file:
        print(line)

# ------------------ hashlib module -------------- #
import hashlib

m = hashlib.md5()

with open('test.txt', 'rb') as file:
    data = file.read()
    m.update(data)
    print(m.hexdigest())

with open('/Users/jinglu/Desktop/JingLu-SoftwareEngineer-CoverLetter.pdf', 'rb') as my_file:
    data = my_file.read()
    print(data)


