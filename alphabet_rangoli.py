import string
alpha = string.ascii_lowercase
n = 25
new_result1 = ""
longest = n + n - 1 + ((n + n - 1) - 1)
for i in range(1, n + 1):
    result = ""
    new_result1 = ""
    index = n - 1
    for j in range(1, (i * 2 - 1) +1 ):
        if j > i:
            result += str(alpha[index]) + "-"
            index += 1
        if j == i:
            result += str(alpha[index]) + "-"
            index += 1
        if j < i:
            result += str(alpha[index]) + "-"
            index -= 1
    for letter in range(len(result)-1):
        new_result1 += result[letter]
    print(new_result1.center(longest, "-"))
    #print(result.center(n*3+3, "-"))

for i in range(n - 1, 0, -1):
    result = ""
    new_result2 = ""
    index = n - 1
    for j in range((i * 2 - 1) - 1, -1, -1):
        if j > i:
            result += str(alpha[index]) + "-"
            index -= 1
        if j == i:
            result += str(alpha[index]) + "-"
            index -= 1
        if j < i:
            result += str(alpha[index]) + "-"
            index += 1
    for letter in range(len(result) - 1):
        new_result2 += result[letter]


    print(new_result2.center(longest, "-"))



'''    
  2
 212
21012
'''