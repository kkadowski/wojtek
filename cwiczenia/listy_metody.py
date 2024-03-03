''' 
Metody w listach
K>K> 2023-10-11
v. 1.0
'''

l1 = [ 2, 4, 5, 6, 7, 8, 8, 9 ]
print(type(l1))

l1.append(99)
print(l1)

l1.pop()
print(l1)

# l1.insert(1, 99)
# print(l1)

# l1.remove(8)
# print(l1)

#l1 = list(set(l1)) # rzutujesz na set (usuwając powtórki) i potem na list
#print(l1)
l2 = [88,99,100]

l1.extend(l2)
print(l1)

l1.reverse()
print(l1)

dl = len(l1)
print(dl)

dl1 = len("lkjadgsfla")
print(dl1)












