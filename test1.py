def addTwo (a, b):
  return a + b

def divide (a, b):
  return a / b, a % b

def isEven (x):
  return (x % 2 == 0)

def gcd (m, n):
  while (m != n):
    if (m > n):
      m = m - n
    else:
      n = n - m
  return m

def coPrime (a, b):
  if (gcd(a, b) != 1):
    return
  else:
    print (a, "and", b, "are co-prime")

def main():
  x = 7
  y = 10

  z = addTwo (x, y)

  p, q = divide (x, y)

  if (isEven(z)):
    print (z)
    
  coPrime (x, y)

main()