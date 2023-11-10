x = 101

def is_prima (n):
  for i in range(2, n):
    if n % i == 0:
      return False

  return True

for i in reversed(range(0, x)):
    y = is_prima(i)
    if y == False or i == 1:
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar", end=", ")
        elif i % 3 == 0:
            print("Foo", end=", ")
        elif i % 5 == 0:
            print("Bar", end=", ")
        elif i == 1:
            print(1)
        else:
            print(i, end=", ")
            
        