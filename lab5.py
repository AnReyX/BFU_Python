from os.path import isdir, isfile, getsize
from os import listdir, mkdir
from pathlib import Path
import shutil


def readFile(filename):
    out = []
    with open(filename) as f:
        for i in f:
            out += [i.strip()]
        return out


def writeFile(filename, content):
    with open(filename, "w") as f:
        for i in content:
            f.write(f"{i}\n")


def task1():
    writeFile("input1.txt", ["1 2 3 3 2 1 1 1 1 1"])
    line = readFile("input1.txt")[0].split()
    print(line)
    ans = 1
    for i in line:
        ans *= int(i)
    writeFile("output1.txt", [str(ans)])
    print(ans)


def task2():
    writeFile("input2.txt", ["1", "9", "-2", "5", "42", "-42", "10", "69", "70", "0"])
    ans = sorted(readFile("input2.txt"), key=int)
    writeFile("output2.txt", ans)
    print(ans)


def task3():
    writeFile("input3.txt",
              ["Ivanov Ivan 5", "Petrov Petr 4", "Vanechkin Vanya 3", "Belkin Bogdan 6", "Zaykin Vladimir 2"])
    sp = sorted(readFile('input3.txt'), key=lambda x: x.split()[2])
    writeFile("output31.txt", [sp[0]])
    writeFile("output32.txt", [sp[-1]])
    print(sp[0], sp[-1])


# Lab 1. P4D
def task_1(inp_path=Path.cwd()):
    if isdir(inp_path):
        f = False
        files = listdir(inp_path)
        for i in files:
            if getsize(f"{inp_path}\{i}") < 2 * 1024:
                print(i)
                f = True
        if not f:
            print("No files found.")
        else:
            new_path = f"{inp_path}\small"
            mkdir(new_path)
            for i in files:
                shutil.copy(i, new_path)
    else:
        print("Error! No such directory.")


def task_2(dirpath=Path.cwd(), files):
    Exists = []
    notExists = []
    for i in flies:
        if isfile(f'{dirpath}\{i}'):
            Exists += [i]
        else:
            NotExists += [i]
    writeFile("ex.txt", Exists)
    writeFile("nex.txt", NotExists)
    print(Exists, NotExists)


task3()