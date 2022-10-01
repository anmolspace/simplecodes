
import sympy as s  #Use sympy to check prime because it checks faster
files = open("C:") #Location of the txt file containing the digits of pi
pi = files.read()
files.close()
def pin(n):
  size = len(pi)
  for i in range(2, size-n):
      p = pi[i:i+n]
      if p[0] in str('1379'):
        if p == p[::-1]:
          if s.isprime(int(p)):
            print(p)
            break

pin(21)
