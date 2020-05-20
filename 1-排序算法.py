# -*- coding:utf-8 -*-
import time
# import numpy as np
# import matplotlib.pyplot as plt
import random

'''
算法名称：选择排序算法

时间复杂度：O(n^2)

作者：张海涛

时间：2020-5-13
'''

def select_Sort(arr):
	newArr = []
	for i in range(len(arr)):
		small_arr = arr[0]
		small_index = 0
		for j in range(1,len(arr)):
			if small_arr >= arr[j]:
				small_arr = arr[j]
				small_index = j			
		newArr.append(arr.pop(small_index))
	return newArr


'''
算法名称：快速排序

时间复杂度：

作者：张海涛

时间：2020-5-13
'''

def quick_Sort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]

		less = [i for i in arr[1:] if i <= pivot]
		
		greater = [i for i in arr[1:] if i > pivot]
		
		return quick_Sort(less) + [pivot] + quick_Sort(greater)


'''
算法名称：生成数组

时间复杂度：O(n)

作者：张海涛

时间：2020-5-13
'''

def make_list():
	arr_list = []
	while True:
		arr = input("请输入数据:")
		if arr == 'quit':
			break
		arr_list.append(int(arr))
	return arr_list


'''
算法名称：生成随机数组

时间复杂度：O(n)

作者：张海涛

时间：2020-5-13
'''

def make_random_list():
	arr_list = []
	num = input("请输入随机生成的数组的数量：")
	for i in range(int(num)):
		arr_list.append(random.randint(0,100))
	return arr_list


arr = make_random_list()
print(arr)
start = time.time()
arr = select_Sort(arr)
print("选择排序：",arr)
end = time.time()
print(end - start)

start = time.time()
arr = quick_Sort(arr)
print("快速排序：",arr)
end = time.time()
print(end - start)



