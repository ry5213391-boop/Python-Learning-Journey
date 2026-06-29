#simple arithmetic module: arithmetic.py

def add(num1, num2):
    return num1 + num2

def square_root(number):
    return number ** 0.5
print(f"__name__ value in arithmetic.py => arithmetic")
#__name__ variable

if __name__ == "__main__":
    a = 10
    b = 20
    result = add(a, b)
    print(result)
    
