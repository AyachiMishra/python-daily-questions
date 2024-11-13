# p1:Write a Python program to sort (ascending and descending) a dictionary by value.
# m1
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# ascending = sorted(d.items(), key = operator.itemgetter())
# descending = sorted(d.items(), key = operator.itemgetter(), reverse = True)

# print(ascending)
# print(descending)

# # m2
# newlist = []


# # p2:write a python to add key to dictionary
# sampledic = {0: 10, 1: 20}
# sampledic['2'] = 30
# print(sampledic['2'])


# # p3: Write a Python script to merge two Python dictionaries.
# # Create the first dictionary 'd1' with key-value pairs.
# d1 = {'a': 100, 'b': 200}

# # Create the second dictionary 'd2' with key-value pairs.
# d2 = {'x': 300, 'y': 200}
# newdic = {}
# for dic in (d1,d2): 
#     newdic.update(dic)

# # print(newdic)


# # p4: write a new python program for traversing dictionary usig fro loop
# d = {'x': 10, 'y': 20, 'z': 30} 

# for dkey, dvalue in d.items():
#     print(dkey, '->', dvalue)

# p5: Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x': 500, 'y': 5874, 'z': 560}
max = min = 500

for value in my_dict.values:
    if value > max:
        max = value
    elif value < min:
        min =value

print(max, min)