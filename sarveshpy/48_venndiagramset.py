a={1,2,3,4,5}
b={4,5,6,7,8}

union=a.union(b) # or apipeb
print(union)

intersection=a.intersection(b) # or a&b
print(intersection)

s=a.difference(b) #b-a
print(s)

symmetric=a.symmetric_difference(b)
print(symmetric)