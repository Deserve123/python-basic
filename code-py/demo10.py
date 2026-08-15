def bubble_sort(list1):
    n = len(list1)
    for i in range(n-1):
        for j in range(n-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]

def select_sort(list1):
    n = len(list1) 
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if list1[min_index]>list1[j]:
                min_index = j        
        if min_index != i :
           list1[min_index],list1[i] = list1[i],list1[min_index]

def quick_sort(list1,start,end):
    left = start
    right = end
    mid = list1[start]
    if start >= end:
        return
    while left < right:
        while list1[right] >= mid and left < right:
            right -= 1
        list1[left] = list1[right]
        while list1[left] <= mid and left < right :
            left += 1
        list1[right] = list1[left]
    list1[start] = mid
    quick_sort(list1,start,left-1)
    quick_sort(list1,right+1,end)

if __name__ == '__main__':
    list1 = [1,5,9,7,6,2,8]
    print(f'排好前:{list1}')
    bubble_sort(list1)
    print(f'冒泡排好后:{list1}')
    select_sort(list1)
    print(f'选择排好后:{list1}')
    quick_sort(list1,0,len(list1)-1)
    print(f'快速排好后:{list1}')