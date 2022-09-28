# the following line reads the list from the input; do not modify it, please
my_numbers = [int(x) for x in input().split(" ")]

# work with the variable 'my_numbers'
new_list = []
for i in my_numbers:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)
