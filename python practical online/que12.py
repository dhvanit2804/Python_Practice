'Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.'

def first_last_same(num_list):

    first = num_list[0]
    last = num_list[-1]

    if first == last:
        return True
    else:
        return False
    
number_X = [10, 20, 30, 40, 10]
print("Result is", first_last_same(number_X))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))