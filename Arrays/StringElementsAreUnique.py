#Algorithm to define if all the elements of a given string are uniques or not
#Using dictionary

def caractersAreUnique (str):
    dic = []
    for x in str:
        if (x in dic):
            return False
        dic.append(x)
    return True



str = "Holass"
print("is unique?: ", caractersAreUnique(str))
