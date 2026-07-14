d = {10:100,20:200,30:300,40:400}
d.update({50:500})
print(d)

d = {10:100,20:200,30:300,40:400}
d[50]= 500 # crepting
d[10] = 100 #updating

del d[30] # deleting
print(d)