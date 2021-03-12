def solution(numbers):
    numbers_str_list = list()
    for i in numbers:
        numbers_str_list.append(str(i))
    sorted_numbers = sorted(numbers_str_list, key = lambda x : x[0])
    answer = ''
    for j in range(len(sorted_numbers) - 1):
        if int(sorted_numbers[j]) // 10 < int(sorted_numbers[j + 1]) // 10:
            sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
    for i in reversed(range(len(sorted_numbers))):
        answer += sorted_numbers[i]
        
    return answer

print(solution([6, 10, 2]))