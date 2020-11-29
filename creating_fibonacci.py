# a = [1,1,2,3,5,8,13,21,34,55,89]


b=[1,1]
for i  in range(100):
    answer=b[-2]+b[-1]
    b.append(answer)
    #print(b)

print(b)