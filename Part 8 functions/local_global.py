n = 1 #Global variable-> it can be accessed inside as well as outside the function.
#local variable means we can access this varible inside the function.
#cant access outside the function.
def fn():
    global n
    n = 5 #local varible
    print("IN", n)
    
fn()
print("OUT", n)