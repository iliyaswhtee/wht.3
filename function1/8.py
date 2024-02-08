def spy_game(nums):
    code = [0, 0, 7]  # The sequence to check for
    index = 0  # Index to keep track of the current element in the sequence
    
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False