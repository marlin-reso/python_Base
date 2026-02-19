def say_Hi(name):
    return f"Hi {name}! "
print(say_Hi("Gara"))

def say_Hi(name):
    return "Hi "+name+"!"
print(say_Hi("Lee"))

def say_Hi(name, age):
    return f"Hi {name}! You are {age} years old."
print(say_Hi("Itachi", 20))

def cube(num):
    return num*num*num
print(cube(3))

def cube(num):
    qube = 1
    for i in range(num):
        qube *= num
    return qube
print(cube(3))


