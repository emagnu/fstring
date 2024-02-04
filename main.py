


import locale



name: str = 'Lele'
value: int = 10


def hello():
    return 'Hello '

def my_square():
    return n_** 2

print(f'Hello {hello()}!')
print('Here is a calculation 20 + 40 = ', str(20+40))
print(f'Here is a calculation 20 + 40 = {20+40}')
print(f'Here is a calculation {20 + 40 = }')

print(f'Here is some data: {value = }')

print(f'This function : {value = }')


name: str = 'Manny'
age: int = 25
weight:float = 55.54321
win_rate: float = 0.678955890123
n_of_friends: int = 63
net_worth: int = 82_981_317_886

print(f'My name is: {name} and my age is: {age} and i weight {weight} Kg')
print(f'My name is: {name} and my age is: {age} and i weight {weight:.2f} Kg')
print(f'I have a win rate of {win_rate:.4%}')
print(f'My name is: {name} and, in Hex, my age is: {age:e} with {n_of_friends:X} or else {n_of_friends:b} in binary') # x=Hex and X representation with ABC... e=Scient notation, O=Oct number b=Binary
print(f'My current net worth is around: £{net_worth:,} ') 
print(f'My current net worth is around: £{net_worth:_} ') 

locale.setlocale(locale.LC_NUMERIC, 'de_DE.utf-8')
print(f'My current net worth is around: Euro{net_worth:n} ') 