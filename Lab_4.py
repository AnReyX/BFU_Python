def task_1():
    d1 = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
    d2 = {'beep' : 'car'}
    d3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
    print(d1.get(input())) # change index after d for different tests


def task_2():
    d1 = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
    d2 = {'beep' : 'car'}
    d3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
    print({val:key for key, val in d1.items()}.get(input())) # change index after d for different tests

# task 3 already done

def task_4():
    d = dict([(i, 0) for i in range(10)])
    for i in input():
        d[int(i)] += 1
    print(sorted(d.items(), key=lambda x: x[1], reverse=True)[:3])


task_1()