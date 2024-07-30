# string_calculator.py

import re

class StringCalculator:

    @staticmethod
    def add(numbers):
        if not numbers:
            return 0
        
        delimiter, numbers = StringCalculator._extract_delimiter(numbers)
        number_list = StringCalculator._split_numbers(numbers, delimiter)
        
        return StringCalculator._calculate_sum(number_list)
    
    @staticmethod
    def _extract_delimiter(numbers):
        if numbers.startswith('//'):
            return StringCalculator._get_custom_delimiter(numbers)
        return ',|\n', numbers

    @staticmethod
    def _get_custom_delimiter(numbers):
        parts = numbers.split('\n', 1)
        custom_delimiter = parts[0][2:]
        if custom_delimiter.startswith('[') and custom_delimiter.endswith(']'):
            custom_delimiter = re.escape(custom_delimiter[1:-1])
        return custom_delimiter, parts[1]

    @staticmethod
    def _split_numbers(numbers, delimiter):
        return re.split(delimiter, numbers)

    @staticmethod
    def _calculate_sum(number_list):
        total = 0
        negatives = []
        
        for num in number_list:
            total, negatives = StringCalculator._process_number(num, total, negatives)
        
        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")
        
        return total
    
    @staticmethod
    def _process_number(num, total, negatives):
        if num:
            n = int(num)
            if n < 0:
                negatives.append(n)
            elif n <= 1000:
                total += n
        return total, negatives
