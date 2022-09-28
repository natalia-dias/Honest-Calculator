msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"


def play(x):
    global n
    if n > 0:
        honest_calc(x)


def count(x, y, oper):
    while True:
        if oper == "/":
            try:
                result = float(x) / float(y)
            except ZeroDivisionError:
                print(msg_3)
                honest_calc(0)
            else:
                store(result)
                break
        elif oper == "+":
            result = float(x) + float(y)
            store(result)
            break
        elif oper == "-":
            result = float(x) - float(y)
            store(result)
            break
        elif oper == "*":
            result = float(x) * float(y)
            store(result)
            break
        else:
            print(msg_2)
            honest_calc(0)
            continue


def honest_calc(mem):
    while True:
        memory = mem
        print(msg_0)
        calc = input().split()
        if calc[0] == "M":
            count(memory, calc[2], calc[1])
        elif calc[2] == "M":
            count(calc[0], memory, calc[1])
        else:
            try:
                calc[0] = float(calc[0])
                calc[2] = float(calc[2])
            except ValueError:
                print(msg_1)
                continue
            else:
                count(calc[0], calc[2], calc[1])


def cont(mem):
    print(msg_5)
    global n
    answer = input()
    while True:
        if answer == "y":
            honest_calc(mem)
        #if answer == "n":
            #n = 0
            #honest_calc(0)
            

def store(result_):
    print(result_)
    memory_ = 0
    print(msg_4)
    answer = input()
    if answer == "y":
        memory_ += result_
        cont(memory_)
    elif answer == "n":
        cont(0)


n = 1
honest_calc(0)
