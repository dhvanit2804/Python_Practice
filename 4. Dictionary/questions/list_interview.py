'''Problem: "Sliding Window Maximum Sum"

You are given a list of integers representing daily sales:
sales = [100, 200, 150, 300, 250, 400, 350]
You need to find the maximum total sales for any 3 consecutive days (a sliding window of size 3).

🎯 Tasks:

Use lists and loops (no numpy or pandas)
Print the maximum sum of 3 consecutive days
Print the starting index of that 3-day window
Optional: Print the 3-day window itself'''

sales = [100, 200, 150, 300, 250, 400, 350]
window_size = 3

max_sum = 0
start_index = 0

for i in range(len(sales) - window_size + 1):
    current_sum = sum(sales[i:i+window_size])
    if current_sum > max_sum:
        max_sum = current_sum
        start_index = i

print("Maximum sales in 3 consecutive days:", max_sum)
print("Starting index of window:", start_index)
print("Window:", sales[start_index:start_index + window_size])