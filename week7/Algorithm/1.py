###input 구현###
lst = list(map(int, input().split()))


### mergeSort 함수의 빈칸 ___를 채워 완성해주세요 ###


def mergeSort(A):
    ### Base case ###
    if len(A) <= 1:
        return A

    ### A를 반으로 쪼개서 recursive call을 해 주고 정렬된 반쪽짜리들을 받아옵니다.
    left = mergeSort(A[: len(A) // 2])
    right = mergeSort(A[len(A) // 2 :])

    ### 여기서부터 두 개의 쪼개졌던 list를 합치는 Merge 부분입니다.
    ### 여기서 포인트는 정렬된 상태로 돌아왔기 때문에 앞에서부터 순차적으로 한번만 돌면 정렬시킬 수 있다는 것입니다.
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    if i == len(left) and j < len(right):  # 만약 left의 원소를 모두 채웠고, right가 남아있을 때.
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    elif j == len(right) and i < len(left):  # 만약 right의 원소를 모두 채웠고, left가 남아있을 때.
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
    return A  # 마지막으로 정렬된 list를 리턴합니다.


###output 구현###
ans = mergeSort(lst)
for i in range(len(ans)):
    print(ans[i])
