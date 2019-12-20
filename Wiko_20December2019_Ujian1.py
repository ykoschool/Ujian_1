# Soal 1
def hashtag(string):
    empty = []
    emptystr = ""
    if string == "":
        print(False)
        return False
    elif len(string) > 140:
        print(False)
        return False
    a = string.split(' ')
    for tes in a:
        empty.append(tes.capitalize())
        
    emptystr = emptystr.join(empty)
    print("#" + emptystr)
    
        

hashtag("hello world this is my python     examination")
hashtag('More than 140 characters sakjdfksdjfhksdjhfksdjhfksdjfhdksjfhsjdkfhskdjhfdksjhfkjsdhfksjdhfksjdhfkjsdhfkajkfhkdjsfhkjsdhfksdjhfjksdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfkjsdhfksjdhjdshfkjdshfkjdshf')
hashtag("")


# Soal 2
def phone(number):
    if len(number) == 10:
        print("'" + "(" + str(number[0]) + str(number[1]) + str(number[2]) + ")" + " " + str(number[3]) + str(number[4]) + str(number[5]) + "-" + str(number[6]) + str(number[7]) + str(number[8]) + str(number[9]) + "'" )
    else:
        return False

phone([1,2,3,4,5,6,7,8,9,0])
phone([1,2,3,4,5,6,7,8,9,0,15,6])


# Soal 3

def sort(num):
    odd = []
    even = []
    new = []
    new2 = []
    for tes in num:
        if tes % 2 != 0:
            odd.append(tes)
        else:
            even.append(tes)
    even.sort(reverse = True)
    odd.sort()
    for tes2 in num:
        if tes2 % 2 !=0:
            new.append('o')
        else:
            new.append('e')
    for i in new:
        if i == "o":
            new2.append(odd[0])
            odd.pop(0)
        else:
            new2.append(even[0])
            even.pop(0)
    print(new2)

    
sort([5, 3, 2, 8, 1, 4])

# Soal 4
#attempt 1
def hollow(height):
    z = ''
    for a in range(1, height):
        for b in range(0,height-a-1):
            z += "_"
        for b in range(0, a):
            z += "_#"
        for b in range(a, height):
            z += "_"
        z += '\n'
    return print(z + '#'*(height*2-1))


## attempt 2
def hollow(height):
    z = ''
    for a in range(1, height):
        for b in range(0,height-a):
            z += "_"
        for b in range(0, 1):
            z += "#"
        for b in range(0, height+a*2-7):
            z += "_"
        for b in range(4, height):
            z += "#"
        for b in range(a, height+a):
            z += "_"
        z += '\n'
    return print(z + '#'*(height*2-1))
# hollow(1)
hollow(2)
hollow(3)
hollow(4)
hollow(5)