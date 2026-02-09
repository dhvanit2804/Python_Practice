'''Given a list:
nums = [1, 2, 2, 3, 4, 4, 4, 5]
Create a dictionary showing the count of each number.'''

nums = [1, 2, 2, 3, 4, 4, 4, 5]

count = {}
 
for n in nums:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

print(count)