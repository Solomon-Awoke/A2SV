
def split_and_join(line):
    
    # Split the string by space
    line = line.split(" ")
    
    # Join the string with "-"
    line = "-".join(line)
    
    return line


input_str = "this is a string"
result = split_and_join(input_str)
print(result)  # Output: "this-is-a-string"
