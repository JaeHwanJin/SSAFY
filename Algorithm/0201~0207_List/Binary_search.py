# 이진 검색
# 자료가 정렬 되어 있을때만 사용
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:  # 검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
        return False  # 검색 실패


# binarySearch()

# def binarySearch2(a, low)
