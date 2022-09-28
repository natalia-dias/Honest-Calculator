seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
days = []
sec_per_day = 86400
for i in seconds:
    d = i / sec_per_day
    days.append(int(d))
print(days)
