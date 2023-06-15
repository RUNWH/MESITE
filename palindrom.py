q=input("введите палиндром: ")
def plndr(q):
    if q==q[::-1]:
        return True
    else:
        return False
    
print(plndr(q))    