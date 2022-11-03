#string basic formatting
name = "John"
age = 23
print("Hello, %s. You are %d." % (name, age))

# name = "John"   

greeting = f"Hello, {name}. You are {age}."
print(greeting)
name = "Rolf"
print(greeting)

#string advanced formatting     

print("Hello, {}. You are {}.".format(name, age))
print(f"Hello,{name}")
print("Hello, {0}. You are {1}.".format(name, age))
print("Hello, {1}. You are {0}.".format(name, age))
print("Hello, {name}. You are {age}.".format(name=name, age=age))