l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}
print(l[0])
print(t[0])
# print(s[0])
#print s is not subscriptable
print(s)
#appending to a list
l.append("Smith")

#adding to a set
s.add("Smith")

#length of a list
print(len(l))
#length of a set    
print(len(s))
#length of a tuple
print(len(t))

# advanced set operations
# find the difference between two sets
friends = {"Rolf", "Bob", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad)
print(local_friends)
# find the union between two sets
local = {"Rolf","Anne"}
abroad = {"Bob", "Anne"}
friends = abroad.union(local)
print(friends)
# find the intersection between two sets
local = {"Rolf","Anne"}
abroad = {"Bob", "Anne"}
friends = abroad.intersection(local)
print(friends)