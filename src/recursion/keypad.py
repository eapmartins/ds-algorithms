def get_characters(num):

    switcher = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    
    return switcher.get(num, "")

def keypad(num):
    
    if num <= 1:
        return [""]

    if 1 < num <= 9:
        return list(get_characters(num))

    last_digit = num % 10
    small_output = keypad(num//10)
    keypad_string = get_characters(last_digit)

    output = list()

    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)

    return output

assert get_characters(1) == ""
assert get_characters(2) == "abc"
assert get_characters(10) == ""
assert keypad(2) == ["a", "b", "c"]
assert sorted(keypad(23)) == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])