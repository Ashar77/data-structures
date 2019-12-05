def remove_duplicates(data):
   print(id(data))
   list_1 = []
   for i in range(len(data)):
       if data[i] not in list_1:
           list_1.append(data[i])
   print(list_1)
   print(id(list_1))
remove_duplicates([1,2,'a',7,2,'a'])


