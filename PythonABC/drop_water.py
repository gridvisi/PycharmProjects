
option = [1.5,3.25,5,6.75]
def pourMin(u,U):
    # u=small, U=larger
    i,j,s = 1,0,True
    ans = [float('INF')]
    minvol = u*i - U*j
    step = 0
    while minvol <= u+U:
        #minvol <= 两个杯子容量之和
        s = not(s)
        minvol = abs(u*i - U*j)
        i += s
        j += not(s)
        ans.append(minvol)
    findMin = [i for i in set(ans)if i in option]
    return sorted(set(ans))[:-2],findMin

u,U = 9,11.25
u,U = 2,3
print(pourMin(u,U))