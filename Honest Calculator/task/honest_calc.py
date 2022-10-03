msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(x):
    if x.is_integer() is True and -10 < x < 10:
        return True
    else:
        return False


def check_test(x, y, oper):
    message = ""
    while True:
        if is_one_digit(x) and is_one_digit(y) is True:
            message = message + msg_6
        if x == 1 or y == 1 and oper == "*":
            message = message + msg_7
        if x == 0 or y == 0 and oper != "/":
            message = message + msg_8
        if message != "":
            print(msg_9 + message)
            break
        else:
            break


result = 0
memory = 0
while True:
# starting Honest Calculator
    while True:
        print(msg_0)
        calc = input().split()
        if calc[0] == "M":
            calc[0] = memory
        if calc[2] == "M":
            calc[2] = memory
        if calc[0] != "M" and calc[2] != "M":
            try:
                calc[0] = float(calc[0])
                calc[2] = float(calc[2])
            except ValueError:
                print(msg_1)
                continue

        check_test(calc[0], calc[2], calc[1])

# getting result
        if calc[1] == "/":
            try:
                result = float(calc[0]) / float(calc[2])
            except ZeroDivisionError:
                print(msg_3)
        elif calc[1] == "+":
            result = float(calc[0]) + float(calc[2])
        elif calc[1] == "-":
            result = float(calc[0]) - float(calc[2])
        elif calc[1] == "*":
            result = float(calc[0]) * float(calc[2])
        else:
            print(msg_2)
            break

# want to store the result
        print(result)
        print(msg_4)
        answer = input()
        if answer == "y":
            if is_one_digit(result) is True:
                print(msg_10)
                answer_2 = input()
                if answer_2 == "y":
                    print(msg_11)
                    answer_3 = input()
                    if answer_3 == "y":
                        print(msg_12)
                        last_answer = input()
                        if last_answer == "y":
                            memory = result
                        elif last_answer == "n":
                            memory = memory
                    elif answer_3 == "n":
                        memory = memory
                elif answer_2 == "n":
                    memory = memory
            else:
                memory = result

# want to continue?
        print(msg_5)
        answer = input()
        if answer == "y":
            continue
        if answer == "n":
            exit(0)
