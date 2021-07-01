def permutations(string):
    
    """
    :param: input string= s
    Return - list of all permutations of the input string
    """

    return return_permutations(string, 0)
    
def return_permutations(string, index):
    output = list()
    
    if index >= len(string):
        return [""]
    
    small_output = return_permutations(string, index + 1)
    
    current_char = string[index] 
    
    for sub_string in small_output:
        
        for index in range(len(small_output[0]) + 1):
            
            new_sub_string = sub_string[0: index] + current_char + sub_string[index:]
            output.append(new_sub_string)

    return output


assert sorted(permutations("abc")) == sorted(['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])