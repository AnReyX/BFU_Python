from os.path import isdir, isfile, getsize, join
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
    print("Входные данные:", line)
    ans = 1
    for i in line:
        ans *= int(i)
    writeFile("output1.txt", [str(ans)])
    print("Result written to output1.txt!", ans)


def task2():
    writeFile("input2.txt", ["1", "9", "-2", "5", "42", "-42", "10", "69", "70", "0"])
    ans = sorted(readFile("input2.txt"), key=int)
    writeFile("output2.txt", ans)
    print("Result written to output2.txt!", ans)


def task3():
    writeFile("input3.txt",
              ["Ivanov Ivan 5", "Petrov Petr 4", "Vanechkin Vanya 3", "Belkin Bogdan 6", "Zaykin Vladimir 2"])
    sp = sorted(readFile('input3.txt'), key=lambda x: x.split()[2])
    writeFile("output31.txt", [sp[0]])
    writeFile("output32.txt", [sp[-1]])
    print("Result written to output31.txt and 32.txt!", sp[0], sp[-1])


# Lab 1. P4D
def task_1(inp_path=Path.cwd()):
    if isdir(inp_path):
        f = False
        files = [f for f in listdir(inp_path) if isfile(join(inp_path, f)) and getsize(join(inp_path, f)) < 2048] # Файлы, меньше 2 Килобайт и не папки
        for i in files:
            print(i)
            f = True
        if not f:
            print("No files found.")
        else:
            new_path = f"{inp_path}\\small"
            if not isdir(new_path): # Создание папки, если её ещё нет
                mkdir(new_path)
                for i in files:
                    shutil.copy(i, new_path)
    else:
        print("Error! No such directory.")


def task_2(files="", dirpath=Path.cwd()): # Запуск не из консоли, чтобы можно всегда проверить работу кода
    # Тестовые файлы: ["24.txt", "25.txt", "txt.txt", "owo.txt"]
    if not files:
        size = 0
        n = 0
        for i in listdir(dirpath):
            size += getsize(i)
            n += 1
        print(f"Amount of files in direction {dirpath}: {n}, Whole size: {size // 1024} Kb.")
        return 0
    Exists = []
    NotExists = []
    for i in files:
        if isfile(join(dirpath, i)):
            Exists += [i]
        else:
            NotExists += [i]
    writeFile("ex.txt", Exists)
    writeFile("nex.txt", NotExists)
    print("Result written to ex.txt and nex.txt! Exists:", Exists, " Not Exists:", NotExists)


def task_3(dirpath=Path.cwd()):
    pathName = join(dirpath, "nex.txt")
    if isfile(pathName):
        with open(pathName) as f:
            for i in f:
                with open(i.strip('\n'), 'w'):
                    pass
    else:
        print("File 'nex.txt' not found!")


"""
# Запись файлов для теста:
with open("24.txt", "w"):
    pass
with open("lol.txt", "w"):
    pass
task_2(["24.txt", "25.txt", "uwu.txt", "lol.txt", "out.txt", "out.wav"])
"""
