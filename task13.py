def get_sum(string):
    total = 0
    for s in string:
        total += int(s)
    return total

data = input('Enter your number, please ').strip().split(" ")
n = get_sum(data[0]) * int(data[1])
while n > 10:
    n = get_sum(str(n))
print(n)