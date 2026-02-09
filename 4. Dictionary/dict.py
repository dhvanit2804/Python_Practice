'What is Dictionary in Python ?'
'''A dictionary is a collection of key-value pairs, where each key is unique, and 
each key is associated with a value. Dictionaries are unordered, mutable, and 
indexed by keys. They are defined using curly braces {} or the dict() constructor.'''

d = {110: "Harshad", 343: "Jainish", 143: "Meet", 155: "Rahul", 167: "Sahil", 767: "Aarti", 228: "Dhvanit"}
print(d)
print(d[228])
print(d.get(767))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(110))
print(d)
print(d.popitem())
print(d)

d1 = {111: "Yash", 222: "Ayushi", 333: "Bhvya", 444: "Aniket", 555: "Henil"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])