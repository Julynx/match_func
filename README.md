# match_func
*Pattern matching as a function.*
```python
from match_func import match

# Use ranges!
age = 20
match(age,
      {range(0, 3):   'Toddler',
       range(3, 14):  'Child',
       range(14, 18): 'Teen',
       range(18, 65): 'Adult'},
      default =       'Elder')
>> 'Adult'

# Use tuples!
name = 'Clara'
match(name,
      {('Laura', 'John', 'Luke'): 'First class',
       ('Clara', 'Nathan'):       'Business',
       ('Jason', 'Mary'):         'Economy'},
      default =                   'Non customer')
>> 'Business'

# Use conditions!
value = 5
match(value,
      {value < 10:        'Small',
       10 <= value <= 20: 'Medium',
       value > 20:        'Large'})
>> 'Small'

# Use types!
something = 'Hello'
match(something,
      {int:     'Its an integer',
       str:     'Its a string'},
      default = 'Its something else')
>> 'Its a string'

# Mix and match!
earnings = 10_000
match(earnings,
      {str:              'Invalid type: str',
       range(0, 5_000):  'Too low',
       5_000:            'Exactly 5k',
       earnings > 5_000: 'Over the top!'},
      default =         f'Invalid value: {earnings}')
>> 'Over the top!'
```