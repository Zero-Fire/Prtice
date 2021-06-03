# # -*- coding: utf-8 -*-
# def bubble_sort(arr):
#     n = len(arr)
#     for j in range(n-1):
#         count = 0
#         for i in range (n-1-j):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#                 count+=1
#         if 0 == count:
#             break
# if __name__=='__main__':
#     arr = [12,35,13,34,33,23,0.1,100,1000]
#     print("原列表为：",arr)
#     bubble_sort(arr)
#     print("排序后的列表为：",arr)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
if __name__=='__main__':
    arr = [12,35,13,34,33,23,0.1,100,1009]
    print(arr)
    bubble_sort(arr)
    print(arr)
