import numpy as np

#Convert base binary to decimal

def convertBinaryDecimal():
    num=101010
    num_arr = list(map(int, str(num)))
    reverse_num = reversed(list(num_arr))
    count=0
    sum_num = 0
    for i in reverse_num:
        print(count)
        n= (pow(2, 3)) * i
        print(f"result: {n} - {i} - {count}")
        count+=1
    # print(sum_num)


convertBinaryDecimal()
