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

for i in range(3):
  print(i)
  print("This is for loop")
  print("It is pretty simple")

i = 0
while True:
  print(i)
  print("This is while loop with break and continue")
  print("It is pretty simple")
  i = i + 1

  if i > 3:
    break

# x = list()와 x = []는 동일하게 작동하는 리스트 정의
# 하지만 x = list(1,2,3)은 안되고 list([1,2,3])으로 써야 한다.
x = list([4,5,3])
y = ["hello"]

print(x + y)
print(x[0])
x[2] = 10
print(x)

num_elements = len(x)
print(num_elements)

for n in x:
  print(n)

print(y.index("hello"))
print("bye" in y)

if "hello" in y:
  print("Hello is in list")

# x = tuple() 또는 x = () 로 정의
# 리스트에서 사용하는 거의 모든 함수나 메쏘드가 튜플에도 적용
# 튜플은 assignment를 할 수 없다 
# 튜플은 x[0] = 10 으로 할 수 없는 immutable 자료형이다. 

# x = dict() 또는 x = {} 으로 정의
# 딕셔너리는 key:value pair로 element를 구성한다. 

x = {
  "name":"Han",
  "age":20,
}

print(x["name"], x["age"])
print("age" in x)
print(x.keys(), x.values())

for key in x:
  print(key, x[key])
  print("key:" + str(key))
  print("value:" + str(x[key]))

x[0] = "Jay"
print(x)  


