import re

def add(numbers):
    if numbers == "":
        return 0
    
    # Check for custom delimiter
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
        numbers = numbers.replace(delimiter, ',')
    else:
        # Replace new lines with commas
        numbers = numbers.replace('\n', ',')
    
    # Split numbers by comma
    num_list = re.split(',|\n', numbers)
    
    # Convert to integers and ignore numbers greater than 1000
    num_list = [int(num) for num in num_list if num and int(num) <= 1000]
    
    # Check for negative numbers
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
    
    return sum(num_list)

