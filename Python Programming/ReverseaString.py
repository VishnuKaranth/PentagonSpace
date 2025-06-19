def revincr(s1):
    nstr = ""
    for i in range(len(s1)):
        nstr = s1[i] + nstr
    return nstr

def revdecr(s1):
    #For decrementing, we will 
    nstr = ""
    for i in range(len(s1) - 1, 0-1, -1):
        nstr = nstr + s1[i]
    return nstr

def revincrrec(s1, nstr, i):
    
    if i >= len(s1):
        return nstr
    nstr = s1[i] + nstr
    return revincrrec(s1, nstr, i + 1)

def recdecrrec(s1, nstr, i):
    if i < 0:
        return nstr
    nstr = nstr + s1[i]
    return recdecrrec(s1, nstr, i - 1)

def revrtrlist(s1):
    #1st way ==> list() Typecasting
    #l1 = list(s1)
    #2nd way ==> Customized List
    l1 = []
    for i in s1:
        l1.append(i)
    i , j = 0, len(l1) - 1
    #Logic to reverse the list
    while i < j:
        l1[i], l1[j] = l1[j], l1[i]
        i += 1
        j -= 1
    #1st way ==> join() method
    #nstr = ''.join(l1)
    #2nd way ==> Customized String
    nstr = ""
    for i in l1:
        nstr += i
    return nstr
s1 = input("Enter a string: ")
print("Original String: ", s1)

res = revincr(s1)
print("Incremented String: ", res)

res = revdecr(s1)
print("Decremented String", res)

res = revincrrec(s1, "", 0)
print("Incremented String using recursion: ", res)

res = recdecrrec(s1, "", len(s1) - 1)
print("Decremented String using recursion: ", res)

res = revrtrlist(s1)
print("Reversed String using list: ", res)


    