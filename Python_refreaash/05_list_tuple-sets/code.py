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