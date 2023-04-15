def fibonacci(number):
    fibonacci_numbers = [0,1]
    total = 1
    for index in range(2, number+1):
      total += index
    return total