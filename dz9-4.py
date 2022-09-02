import random
lst = random.sample(range(1, 20), 10)
mapped_numbers = list(map(lambda x: x * 2 if(x%2==0) else x*3, lst))

print(lst)
print(mapped_numbers)