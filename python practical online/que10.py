'Given a list of integers, find and print both the largest and the smallest numbers.'

nums = [45, 2, 89, 12, 7]
largest = nums[0]
smallest = nums[0]

for i in nums:
    if i > largest:
        largest = i
    
    if i < smallest:
        smallest = i

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")