def sort_numbers(numbers: list[float]):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[len(numbers) // 2]
        less = [i for i in numbers if i < pivot]
        equal = [i for i in numbers if i == pivot]
        great = [i for i in numbers if i > pivot]
        return sort_numbers(less) + equal + sort_numbers(great)
