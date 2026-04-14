empty_tuple = tuple()
Brothers = ('Jaskaran', 'Mankaran', 'Manraj', 'Brady')
Sisters = ('Tanvir',)
Siblings = Brothers + Sisters
print('The number of siblings I have are {}'.format(len(Siblings)))
Siblings = list(Siblings)
Siblings.append('Mom')
Siblings.append('Dad')
family_members = tuple(Siblings)

#level 2
*siblings, mom, dad = family_members
print(siblings)


fruits = ('apple', 'orange', 'banana')
vegetables = ('carrot', 'tomato')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_ls = list(food_stuff_tp)

def slice_out(lst):
    middle = len(lst)//2
    if len(lst) % 2 == 0:
        return lst[middle - 1: middle + 1]
    else:
        return [lst[middle]]
print(slice_out(food_stuff_ls),
food_stuff_ls[:3],
food_stuff_ls[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Does Estonia exist in our nordic countries: {}'.format('Estonia' in nordic_countries))
print('Does Iceland exist in our nordic countries: {}'.format('Iceland' in nordic_countries))




