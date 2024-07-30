

import re

class StringCalculator:
    
    @staticmethod
    def add(numbers):
        if not numbers:
            return 0
        
        delimiter = ',|\n'
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            custom_delimiter = parts[0][2:]
            if custom_delimiter.startswith('[') and custom_delimiter.endswith(']'):
                custom_delimiter = re.escape(custom_delimiter[1:-1])
            delimiter = custom_delimiter
            numbers = parts[1]
        
        number_list = re.split(delimiter, numbers)
        
        total = 0
        negatives = []
        
        for num in number_list:
            if num:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                elif n <= 1000:
                    total += n
        
        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")
        
        return total
