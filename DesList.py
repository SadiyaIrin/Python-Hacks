from collections import Counter

my_supermarket =  ['Cheese', 'Sauces', 'Bread', 'Meat', 'Cheese','Seafood', 'Pasta', 'Meat', 'Cheese', 'Rice', 'Seafood', 'Oils', 'Meat', 'Cheese', 'Sauces', 'Seafood', 'Soups', 'Dairy', 'Cheese', 'Meat', 'Seafood', 'Eggs', 'Dairy','Snacks', 'Seafood', 'Sauces', 'Crackers', 'Dairy', 'Cheese', 'Drinks']

#[('Cheese', 6),('Meat', 4)]

counter_thingy = Counter(my_supermarket)
#print(counter_thingy.most_common())

#print(counter_thingy.most_common(3))

sentence = 'At some point, you may need to break a large string down into smaller chunks, or strings. This is the opposite of concatenation which merges or combines strings into one. To do this, you use the split function. What it does is split or breakup a string and add the data to a string array using a defined separator.'

# 1 - turn it into a list of words
# 2 - turn it into a Counter object
# 3 - Show the most frequent words

words = sentence.split()
counter_thingy = Counter(words)

#print(counter_thingy.most_common())

print(dict(counter_thingy.most_common()))