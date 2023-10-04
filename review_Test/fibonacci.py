import random

def generate_fib(n):
    nums = [0, 1]
    
    while len(nums) < n:
        next_number = nums[-1] + nums[-2]
        rand = random.randint(1, 100)
        nums.extend([next_number, rand])
    
    return nums

n = 10 
fibonacci_nums = generate_fib(n)
print(fibonacci_nums)
