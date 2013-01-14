import sys

def fib(n):

    if n <= 2 :
        return 1

    return fib(n-1) + fib(n-2)

def main(n):

    i = 0
    while 1 :
        print fib(i)
        i += 1

if __name__ == "__main__":
    main(*sys.argv)
      



