from random import randint
def random_user_id():
    string = []
    useable = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(6):
        char = randint(0, 35)
        string.append(useable[char])
    return "".join(string)
print(random_user_id())

def user_id_gen_by_user():
    length = int(input('Enter length of id: '))
    amount = int(input('Enter total number of ids:'))
    strings = []
    for i in range(amount):
        string = []
        useable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        for i in range(length):
            char = randint(0, 61)
            string.append(useable[char])
        print("".join(string))
user_id_gen_by_user()

def rgb_color_gen():
    rgb = []
    for i in range(3):
        color = randint(0, 255)
        rgb.append(color)
    return tuple(rgb)
print(rgb_color_gen())

def generate_colors(type, amount):
    if type == 'hexa':
        result = []
        useable = '1234567890abcdef'
        for i in range(amount):
            string = []
            for j in range(5):
                char = randint(0, len(useable) - 1)
                string.append(useable[char])
            result.append("#" + "".join(string))
        return result
    elif type == 'rgb':
        result = []
        for i in range(amount):
            string = []
            for j in range(3):
                char = randint(0, 255)
                string.append(str(char))
            result.append("rgb(" + ("".join(string)) + ")")
        return result
    else:
        return("please enter a valid input")

print(generate_colors('rgb', 8))

def shuffle_list(array):
    result = []
    length = len(array) - 1
    for i in range(length):
        shuffle = randint(0, length)
        result.append(array[shuffle])
        array.pop(shuffle)
        length -= 1
    result.extend(array)
    return result
array = [1, 2, 3, 4, 5, 6]
print(shuffle_list(array))

def random_digits():
    result = set()
    while len(result) < 7:
        char = randint(0, 9)
        result.add(char)
    return list(result)
print(random_digits())
    





