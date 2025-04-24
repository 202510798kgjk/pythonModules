minNum, maxNum=input().split()
minNum=int(minNum); maxNum=int(maxNum)

if(1<=minNum and minNum<=1000000000000 \
   and minNum <= maxNum and maxNum <= minNum + 1000000):
    count=0
    for i in range(minNum, maxNum+1):
        j=2
        while i>=(j**2):
            if i%(j**2)==0:
                break
            j+=1
        else:
            continue
        count+=1

print(count)
