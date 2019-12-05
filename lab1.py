dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
dict4 = {}


dic4 = {}
for n in (dict1,dict2,dict3):
    dict4.update(n)
    

print(id(dict1))
print(id(dict2))
print(id(dict3))
print(id(dict4))


for x in dict2.items():
    print(x)
    print(id(x))




l1 = [2,991,2,3,1,4,5,2,7,2]

l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)

print(l2)

# l1 = [1,8,'a',6,(2,1),7,9]
# count = 0
# for x in l1:
#     if type(x) is not tuple:
#       count+=1
#     else:
#         print(id(x))
#         break

# print(count)
# print(id(l1))

