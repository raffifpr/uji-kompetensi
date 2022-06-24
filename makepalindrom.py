n = int(input())
y = ["" for i in range (2*n-1)]
for i in range (n):
    x = input()
    y[i] = y[2*n-i-2] = x
result = ""
for i in y:
    result += i
print (result)
