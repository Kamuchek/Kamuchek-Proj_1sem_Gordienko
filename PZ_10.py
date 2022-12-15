veg = {'молоко','соль','сахар','мясо','сыр'}
list_a = {'молоко', 'соль','сахар'}
list_b = {'мясо','молоко','сыр'}
print ("полный перечень всех товаров",veg)
list_a = ['молоко', 'соль','сахар']
list_b = ['мясо','молоко','сыр']
list_c = list()
list_g = list()
for template in list_a:
    if template not in list_b:
        list_c.append(template)
for template in list_b:
    if template not in list_a:
        list_g.append(template)
print("в магните нет",list_c)  
print("в пятерочке нет",list_g)  
