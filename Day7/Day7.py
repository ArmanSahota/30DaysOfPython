it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print('IT company length: ', len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Palentir', 'Databricks'])
print(it_companies)
it_companies.remove('Palentir')
print(it_companies)
# diff between remove and discard is that discard does not bring up an error if the item in the function is not in the list
it_companies.discard('Palentir')

a = {'a', 'b,','c'}
b = {'c', 'd', 'e', 'f'}
c = a.union(b)
print(c)
print(a.intersection(b))

print(' is a subset b?: ', a.issubset(b))
print('is a and b a disjointed set? ', a.isdisjoint(b))
a.union(b)
b.union(a)
print('the symmetric diff of a and b is : ', a.symmetric_difference(b))

del a
del b
del c

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)

print('which is the set bigger than the list', len(age_set) > len(age) )

#string is data storied in memory

#list is a group of unordered, mutable items that may have duplicates

#tuple immutable list of items meaning you can't change them once they are added. 

#set a list of unordered mutable items without duplicates

my_string = 'I am a teacher and I love to inspire and teach people.'
my_list = my_string.split(' ')
my_set = set(my_list)
print('The number of uniqe words is: ', len(my_set))
