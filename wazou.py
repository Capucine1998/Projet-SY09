#We print the sum of the 6 first values of fibonacci sequence
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    sum = 0
    for i in range(6):
        sum += fib(i)
    print(sum)

if __name__ == "__main__":
    main()

