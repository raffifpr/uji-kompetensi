n = 5
y = [" " for i in range (2*n-1)]
for i in range (n):
    x = i+1
    y[i] = y[2*n-i-2] = x
    result = ""
    for j in y:
        result += str(j)
    print (result)
for i in range (n-1,0,-1):
    y[i] = y[2*n-i-2] = " "
    result = ""
    for j in y:
        result += str(j)
    print (result)
