# 오름차순
# def Selection_Sort(arr):
#     for i in range(len(arr) - 1):
#         minIdx = i
#         for j in range(i + 1, len(arr)):
#             if arr[minIdx] > arr[j]:
#                 minIdx = j
#
#         arr[i], arr[minIdx] = arr[minIdx], arr[i]
#     return arr


# 내림차순
# def Selection_Sort2(arr):
#     for i in range(len(arr) - 1):
#         maxIdx = i
#         for j in range(i + 1, len(arr)):
#             if arr[maxIdx] < arr[j]:
#                 maxIdx = j
#
#         arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
#     return arr


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(Selection_Sort2(arr))

