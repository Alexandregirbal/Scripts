
from time import perf_counter
import sys
from colors import Colors, colorize
def Perf(func):
    def wrapper(*args, **kwargs):
        startTime = perf_counter()
        func(*args, **kwargs)
        endTime = perf_counter()
        print(colorize(f"Function '{func.__name__}' took {round(endTime-startTime,2)}secs to execute.",Colors.Yellow))
    return wrapper

#TEST
if __name__ == '__main__':
    @Perf
    def test(max):
        a = 1
        for _ in range(1,max**8):
            a += 1
        print(a)
    test(10)