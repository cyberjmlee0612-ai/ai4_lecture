import random
numbers = [random.randint(1,100) for i in range(10)]
numbers[1] = numbers[-1]
numbers[-1] = numbers[1]
print(numbers[1])
