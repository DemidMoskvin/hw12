def sorty(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a
test1 = [5,3,2,4,1]
test2 = [1,2,3,4,5]
test3 = [1,3,4,-5,6,0,-3,1]
test4 = [0,-1,1,2,-2]
print(sorty(test1))
print(sorty(test2))
print(sorty(test3))
print(sorty(test4))