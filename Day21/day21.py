from collections import Counter
class Statistics:
    def __init__(self, ls:list):
        self.ls = ls
        
    def count(self):
        return len(self.ls)
    def sum(self):
        res = 0
        for i in self.ls:
            res += i
        return res
    def min(self):
        sortls = sorted(self.ls)
        return sortls[0]
    def max(self):
        sortlsR = sorted(self.ls, reverse=True)
        return sortlsR[0]
    def range(self):
        sortls = sorted(self.ls)
        return (sortls[-1] - sortls[0])
    def mean(self):
        return self.sum() / self.count()
    def median(self):
        sortls = sorted(self.ls)
        if self.count() % 2 == 0:
            L = sortls[self.count()//2]
            R = sortls[(self.count()//2) - 1]
            return ((L + R) / 2)
        else:
            return sortls[self.count()//2]
    def mode(self):
        
        Cls = Counter(self.ls)
        element, c = Cls.most_common(1)[0]
        return {'mode': element, 'count': c}
    
    def var(self):
        mean = self.mean()
        total = 0

        for number in self.ls:
            difference = number - mean
            total += difference ** 2

        # Population variance, matching the exercise output
        return total / self.count()

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        counts = Counter(self.ls)
        result = []

        for number, count in counts.items():
            percentage = count / self.count() * 100
            result.append((percentage, number))

        return sorted(result, reverse=True)
    def describe(self):
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {round(self.mean())}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()}\n"
            f"Variance: {round(self.var(), 1)}\n"
            f"Standard Deviation: {round(self.std(), 1)}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )    
    
ages = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
    27, 24, 32, 33, 27, 25, 26, 38, 37, 31,
    34, 24, 33, 29, 26
]

data = Statistics(ages)

print('Count:', data.count())
print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Range:', data.range())
print('Mean:', data.mean())
print('Median:', data.median())
print('Mode:', data.mode())
print('Standard Deviation:', data.std())
print('Variance:', data.var())
print('Frequency Distribution:', data.freq_dist())

data = Statistics(ages)
print(data.describe())

    

class PersonAccount:
    def __init__(self, firstname='Arman', lastname= 'Sahota'):
        self.firstname = firstname
        self.lastname = lastname
        self.expense = {}
        self.incomes = {}
    def total_income(self):
        return sum(self.incomes.values())
    def total_expense(self):
        return sum(self.expense.values())
    def account_info(self):
        return {'name' : (f'{self.firstname} {self.lastname}'), 'income' : self.total_income(), 'expense' : self.total_expense() }
    def add_income(self, description, amount):
        self.incomes[description] = amount
    def add_expense(self, description, amount):
        self.expense[description] = amount
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
person = PersonAccount("John", "Doe")

person.add_income("Salary", 5000)
person.add_income("Freelancing", 1200)
person.add_income("Stocks", 800)

person.add_expense("Rent", 300)
person.add_expense("Food", 150)

print(person.total_income())
print(person.total_expense())
print(person.account_balance())
print(person.account_info())