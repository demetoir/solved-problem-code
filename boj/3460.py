﻿for i in range(int(input())):a=[i for i in bin(int(input()))[2:]];a.reverse();print(" ".join([str(i) for i in range(len(a))if a[i]=="1"]))