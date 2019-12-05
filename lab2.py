# def ins(Dict,key,value):
#     Dict[key] = value
#     print(Dict)

# ins({'a':'naam'},'status','student')


def dele_dictionary(Dict,value,key):
    Dict_2={}
    for each_value,each_key in Dict.items():
        if each_value != value and each_key != key:
            Dict_2[each_key] = each_value
    print(Dict_2)    

dele_dictionary({'name':'amir','age':17},'name','amir')


d = {'name':'amir','age':17}
del d['name']
print(d)











# d = {'name':'aka','age':19}

# for each_value,each_key in d.items():
#     if d['name'] in d:
#         print('yws')
#     print(each_value)
#     print(each_key)
    
# d['z'] = 'kami'




# print(d)


