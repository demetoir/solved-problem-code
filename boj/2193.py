﻿m={0:1,1:1}
def f(n):
    if n not in m:m[n]=f(n-1)+f(n-2)
    return m[n]
print(f(int(input())-1))