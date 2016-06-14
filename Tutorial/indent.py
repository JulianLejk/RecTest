
def fib(n):

        if n > 1 :
            print 'n = ', n
            return n*fib(n-1)
        else:
            print __name__
            return 1
fib(5)