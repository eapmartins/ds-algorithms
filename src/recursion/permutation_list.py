"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy

def permute(input_list):
    

    permutations = []
    
    if len(input_list) == 0:
        permutations.append([])
        
    else:
        first_element = input_list[0]
        rest_list = input_list[1:]
        
        sub_permutations = permute(rest_list)
        
        for a_list in sub_permutations:
            
            for j in range(0, len(a_list) + 1): 
                
                b_list = copy.deepcopy(a_list)  
                b_list.insert(j, first_element)
                permutations.append(b_list)
                
    return permutations

assert permute([1, 0]) == [[1, 0], [0, 1]]
assert permute([0, 1, 2]) == [[0, 1, 2], [1, 0, 2], [1, 2, 0], [0, 2, 1], [2, 0, 1], [2, 1, 0]]