x, y = "Hello", "Bye" 

z = """
Hello python
"""

print(x, y, z)

""" 데이터 타입이 같아야 사칙연산이 가능하므로 casting을 통해 형변환 """
print("How old are you" + str(4)) 

x1, y1 = 4, "4"
print(x1 + int(y1))
print(str(x1) + y1)

if not 1 > 2:
  print("Hello")
elif x1 == 4:
  print("Hi")
else:
  print("Bye")

def chat(name1, name2, age):
  print("Hello? How old are you? %s" %name1)
  print("Me? I am %d %s" %(age, name2))

chat("Alex", "John", 40)

def dsum(a, b):
  result = a + b 
  return result

a, b = 1, 2 
c = a + b 
x, y = 1, 2
z = x + y 

d = dsum(1, 2)
print(d)


# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 안녕이라고 말해라
# 나이가 10살에서 20살 사이면 안녕하세요
# 그외에는 안녕하십니까 라고 말해라 

def sayHello(name, age):
  if age < 10:
    print("Hi," + name)
  elif age <=20 and age >= 10:
    print("Hello," + name)
  else:
    print("Hello Sir")

sayHello("Alex", 9)
sayHello("John", 18)
sayHello("Paul,", 45)
