'''
    T.M
    Homework #1.2
'''

numbers = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 16:'g', 17:'h', 18:'i', 19:'j', 20:'k', 21:'l', 22:'m', 23:'n', 24:'o', 25:'p', 26:'q', 27:'r', 28:'s', 29:'t', 30:'u', 31:'v', 32:'w', 33:'x', 34:'y', 35:'z', 36: '!', 37: '@', 38: '#', 39: '$', 40: '%'}
# 35-ს ზემოთ შემოვიტანოთ პირობითი აღნიშვნები

reversed_numbers = {v: k for k, v in numbers.items()}

base_length = len(numbers) + 10 
# numbers + 0-9-ს ჩათვლით

def decimal_to_any_base(n, base):
  if base > base_length:
    return "Maximum base is {}".format(base_length)
  if base <= 1:
    return "Base shouldn't be less than 2"

  num = []
  while n >= 1:
    num.append(numbers.get(n % base, str(n % base)))
    n = n // base

  result = ''.join((str(x) for x in num))
  return result[::-1].upper()


def base_to_decimal(num, base):
  if base > base_length:
    return "Maximum base is {}".format(base_length)
  if base <= 1:
    return "Base shouldn't be less than 2"

  num = str(num)
  result = 0
  for d, c in enumerate(num):
    n = len(num) - d - 1
    digit = int(reversed_numbers.get(c.lower(), str(c)))
    # დაბლა მოცემულია ფორმულა, რომელითაც შესაძლებელია ნებისმიერი სისტემიდან ათობითში გადაყვანა
    value = digit * base**n
    result += value

  return result


print("Any Base Converter:")
print("0: for decimal to any base")
print("1: for any base to decimal")
x = int(input("Your Choice: " ))

if x == 0:
    num = int(input("Number: "))
    base = int(input("Base: "))
    print(decimal_to_any_base(num, base))
else:
    num = str(input("Number: "))
    base = int(input("Base: "))
    print(base_to_decimal(num, base))



