def task1(s):
    string = s
    n = 0
    curr = string[0]
    for i in string:
        if curr == i:
            n += 1
        else:
            print(curr if n == 1 else f"{curr}{n}", end="")
            curr = i
            n = 1
    print(curr if n == 1 else f"{curr}{n}", end="")


def task1_1(s):
    st = s
    for i in range(len(st) - 1):
        if st[i].isalpha():
            print((st[i] * int(st[i + 1])) if st[i + 1].isdigit() else st[i], end="")
    print(st[-1] if st[-1].isalpha() else "")


def task2(s):
    st = list(s.replace(" ", ""))
    ans = []
    for i in set(st):
        ans += [i]
    print(sorted(ans, key=lambda x: (-st.count(x), x))[:3])


def task3(n):
    num = n.rjust(3, "0")
    d = {
    '1': "один",
    '2': "два",
    '3': "три",
    '4': "четыре",
    '5': "пять",
    '6': "шесть",
    '7': "семь",
    '8': "восемь",
    '9': "девять",
    '10': "десять",
    '11': "одинадцать",
    '12': "двенадцать",
    '13': "тринадцать",
    '14': "четырнадцать",
    '15': "пятнадцать",
    '16': "шестнадцать",
    '17': "семнадцать",
    '18': "восемнадцать",
    '19': "девятнадцать",
    '20': "двадцать",
    '30': "тридцать",
    '40': "сорок",
    '50': "пятьдесят",
    '60': "шестьдесят",
    '70': "семдесят",
    '80': "восемдесят",
    '90': "девяносто",
    '100': "cто",
    '200': "двести",
    '300': "триста",
    '400': "четыреста",
    '500': "пятьсот",
    '600': "шестьсот",
    '700': "семьсот",
    '800': "восемьсот",
    '900': "девятьсот",
    '1000': "тысяча",
    '0': "",
    '00': "",
    '000': ""
    }

    if num in d:
        print(d[num])
    else:
        a = d[num[0] + "00"]
        b = d[num[1:3]] if num[1:3] in d else d[num[1] + "0"]
        c = "" if num[1:3] in d else d[num[2]]
        print((a + (" " if b else "") + b + " " + c).strip())


# task1("aBBcccDDDDeffF") # aB2c3D4ef2F

# task1_1("Y4g2ke3A3BV") # YYYYggkeeeAAABV

# task2("OOO A B C D E A B C D A B C A B A OO") # ['A', 'O', 'B'] - Sort alphabetically if same amount

# task3("5") # пять
# task3("15") # пятнадцать
# task3("55") # пятьдесят пять
# task3("500") # пятьсот
# task3("505") # пятьсот пять
# task3("515") # пятьсот пятнадцать
# task3("555") # пятьсот пятьдесят пять