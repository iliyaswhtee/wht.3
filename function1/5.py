from itertools import permutations

def print_permutations(string):
    perm_list = list(permutations(string))
    
    for perm in perm_list:
        print(''.join(perm))

# Example:
user_input = input("Enter a string: ")
print_permutations(user_input)