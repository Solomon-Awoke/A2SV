def swap_cases(input_string):
    swapped_string = ""
    for char in input_string:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char  # Keep non-alphabetic characters unchanged
    return swapped_string

# Example usage:
input_str1 = "Www.HackerRank.com"
input_str2 = "Pythonist 2"

result1 = swap_cases(input_str1)
result2 = swap_cases(input_str2)

print(result1)  # Output: "wWW.hACKERrANK.COM"
print(result2)  # Output: "pYTHONIST 2"
