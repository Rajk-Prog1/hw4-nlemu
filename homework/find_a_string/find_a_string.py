def find_a_string(original_str: str, substr: str) -> int:
    number = 0
    if substr == "":
        number = number
    else:
        for i in range(0, len(original_str) - len(substr) + 1):
            if substr == original_str[i: i + len(substr)]:
                number = number + 1
    return number


def find_sum (*numbers):
    result = 0

    for num in numbers:
        result = result + num

    print("The result of the numbers is:", result)

find_sum(3, 4, 10)



# In this task, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.





