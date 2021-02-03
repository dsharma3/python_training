str = "This is testing"

def recursiveFunc(str):
    if len(str) == 0:
        return ""
    return recursiveFunc(str[1:]) + str[0]

print(recursiveFunc(str))