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
