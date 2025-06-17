n = int(input("Введите аргумент (число):"))


def fizz_buzz(n):
    for k in range(1, n + 1):
        if k % 3 == 0 and k % 5 == 0:
            print(f"{k} - FizzBuzz")
        elif k % 3 == 0:
            print(f"{k} - Fizz")
        elif k % 5 == 0:
            print(f"{k} - Buzz")
        else:
            print(k)


fizz_buzz(n)
