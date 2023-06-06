names = ['Bob', 'Alice', 'Jane', 'Fred']
ages = [18, 31, 16, 47]

people = {'Bob': 18, 'Alice': 31, 'Jane': 16, 'Fred': 47}

print(names)
print(ages)
print(people)
print()

print(people['Bob'])

partners = {'Bob': 'Alice', 'Jane': 'Heather', 'Fred': 'John'}
print(partners['Jane'])

finish_order = {1: 'Bob', 2: 'Fred', 3: 'Bill'}
print(finish_order[2])

finish_order[4] = 'Jason'
print(finish_order)

finish_order[2] = 'Frederick'
del finish_order[1]
print(finish_order)


# Sometimes, it might be useful to get the key from the value!
# In other words, instead of asking 'Who finished second?', once might ask, 'Where did Jason finish?'
#
# One way of doing this is as follows:
# (i) get the keys and values of the dictionary and put them into a new lists (value_list, key_list)
# (ii) search that new value_list list for the value one is interested in (‘Jason’), and get the index in that list.
# (iii) get the key by choosing the corresponding index from the key_list

print()
finish_order = {1: 'Jean', 2: 'Mary', 3: 'Bill', 4: 'Jason', 5: 'Alice', 6: 'George'}
print(finish_order)
value_list = list(finish_order.values())
key_list = list(finish_order.keys())
index = value_list.index('Jason')
place = key_list[index]
print(f"Jason finished in {place}th place.")

# This is a bit obtuse, and sounds like something that we might want to do all the time.  So, we
# could write a simple function to do it:
#
# N.B.  This function will return the key of the FIRST occurrence of the value in the dictionary

def get_key(dictionary, val):
    for key, value in dictionary.items():
        if value == val:
            return key
    return "key does not exist!"


print(f"Jason finished in {get_key(finish_order,'Jason')}th place.")
