import colorama
from decimal import Decimal, getcontext
import math
import time

def cals(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0

    for k in range(n):
        t = (Decimal(-1)**k)*(math.factorial(6*k))*(13591409+545140134*k)
        deno = math.factorial(3*k)*(math.factorial(k)**(Decimal(3))*(640320**(3*k)))
        pi += Decimal(t)/Decimal(deno)
        pi = pi *Decimal(12)/Decimal(640320**Decimal(1.5))
        pi = 1/pi
        return str (pi)


number = int(input("Please enter thr numer of decimal places to calculate pi: "))
getcontext().prec = number
print(time.time())
start_time = time.time()



print(cals(1))
print(colorama.Fore.BLUE +"Time taken: ", time.time()-start_time)
