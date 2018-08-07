

l1 = [1,2]
l2 = [3,4]
#my_l = lambda l, m: [i*2 for i in ( [y*2 for y in  l2])]
#my_l = lambda l,m : [l[0]+m[0], l[1]+m[1]]
#print(my_l(l1,l2))

def sum_1(a,b):
    l = len(a)
    nl = []
    for x in range(l):
        nl.append(a[x]+ b[x])
    print(nl)

print(sum_1(l1, l2))

