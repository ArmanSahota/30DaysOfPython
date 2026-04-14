empty_list = []
big_list = [1, 2, 33, 4, 5, -1, 23, 235, 54, 11]
print(len(big_list))
print(big_list[0], big_list[(len(big_list)//2)], big_list[-1])

mixed_data = ['arman', 20, 5.09, False, 'Seattle']
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[(len(big_list)//2)], it_companies[-1])
it_companies[0] = 'Nintendo'
print(it_companies)
it_companies.append('Meta')
it_companies.insert((len(it_companies)//2), 'Jira')
it_companies[0] = it_companies[0].upper()
print(it_companies)
string = '#; '.join(it_companies)
print(string)
print('NINTENDO' in it_companies)

it_companies.sort()
print(it_companies)
reverse_sorted_it = it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[3: -3])
it_companies.remove(it_companies[0])
del it_companies[(len(it_companies))// 2]
del it_companies[-1]
it_companies.clear()
print(it_companies)
del it_companies


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()

# part 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(ages)
if len(ages) % 2 == 0:
    print(len(ages)//2)
    print('median age is', ((ages[len(ages)//2]) + (ages[(len(ages)//2) - 1]))// 2)
else:
    print('median age is', ages[len(ages)//2])

print('Average age is ', (sum(ages) / len(ages)))

print('range of ages is ', (max_age - min_age))

min_range = abs(min_age - (sum(ages) / len(ages)))
max_range = abs(max_age - (sum(ages) / len(ages)))
print('The difference between the average, youngest and biggest is: ', min_range, max_range)
import countries
print(countries.countries[len(countries.countries)// 2])
list1 = countries.countries[:len(countries.countries)// 2]
list2 = countries.countries[(len(countries.countries)// 2):]

counties = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
chi, rus, usa,*scandic = counties
print(chi, rus, usa, scandic)


def get_middle(lst):
    middle = len(lst) // 2
    if len(lst) % 2 == 0:
        return lst[middle - 1: middle + 1]
    else:
        return lst[middle]

print(get_middle([1, 2, 3]))        # 2
print(get_middle([1, 2, 3, 4]))     # [2, 3]