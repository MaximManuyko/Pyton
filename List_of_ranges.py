# Реализуйте функцию summary_ranges(), которая находит в списке непрерывные возрастающие последовательности чисел и возвращает список с их перечислением.

# summary_ranges([])
# # []
# summary_ranges([1])
# # []
# summary_ranges([1, 2, 3])
# # ['1->3']
# summary_ranges([0, 1, 2, 4, 5, 7])
# # ['0->2', '4->5']
# summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5])
# # ['110->112', '-5->-4']

def summary_ranges(nums):
    if not nums:
        return []

    result = []
    start = nums[0]
    end = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            start = end = nums[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}->{end}")

    # Добавьте проверку для случаев, когда длина непрерывной последовательности равна 1
    result = [r for r in result if '->' in r]

    return result
