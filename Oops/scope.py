#scopes
#Oop
#Game
wef = "123"
def fn():   
    global wef 
    wef = "456"

fn()
print(wef)