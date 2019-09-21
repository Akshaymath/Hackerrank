def birthdayCakeCandles(ar):
    n=len(ar)
    for i in range(n):
        for j in range (0,n-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
    print(ar)
    count=1
    a=ar[-1]
    for i in range (1,n-1):
        if a==ar[i]:
            count+=1
    return count

ar=[1,2,4,5,6,5,6]
out=birthdayCakeCandles(ar)
print(out)
