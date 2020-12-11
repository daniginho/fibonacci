# a = [1,1,2,3,5,8,13,21,34,55,89]

# 1) I want to be able to generate a number of fibonacci numbers that I input
# 2) I want to have two different modes in the program.  frst one I want to generate numbers
# second one I want to know if a number is fibonacci or not 

# 3) I need a set of instructions in a readme.

def generate(n):
    b=[1,1]
    for i in range(n):
        answer=b[-2]+b[-1]
        b.append(answer)
        #print(b)

    return(b[0:n])

def check(number):
    values = generate(100)

    for i in range(len(values)):
        if number==values[i]:
            return True
        
    return False

print("do you want to generate or check?")
generateorcheck = input()
if generateorcheck=="generate":
    n = int(input("how many numbers?"))
    values = generate(n)
    print(values)
elif generateorcheck=="check":
    n = int(input("what number do you want to check"))
    print(check(n))




