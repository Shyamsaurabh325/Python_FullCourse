# Arithmetic operator
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(20%3)

print(5**2) #5*5
print(6**3) #6*6*6
print(10//2)

# Assignment operator
x=5
print(x)
x=x+5
print(x)
x+=5
print(x)
x-=10
print(x)

# comparison operator
x=10
y=20
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

# Logical operator
#and
x=20
y=10

print(x==20 and x>y)
print(x == 20 and x < y)

# or
print(x==10 or x>y)

# Not
print(not x != 20)
print(not x==20)

# Membership operator
 #In
s1="shyam"
print('m' in s1)
print('s' in s1)
print('q' in s1)
# Not in
print('s'not in s1)
print('q' not in s1)

# Identity operator
# is

x = 10
y = 10
print(x is y, x== y)
print(x is not y , x!= y)

# Bitwise operator
x = 10
y = 8
print(bin(x))      # 1010
print(bin(y))      # 1000
print(bin(x&y),x&y)   # 1000
print(bin(x|y),x|y)   # 1010
print(bin(x^y),x^y)   # 0010

