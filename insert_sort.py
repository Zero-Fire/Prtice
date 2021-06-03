# -*- coding: utf-8 -*-
def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key=arr[i]
        j = i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = key
if __name__=='__main__':
    arr = [12,343,545,3,34,5,67]
    insert_sort(arr)
    print(arr)

