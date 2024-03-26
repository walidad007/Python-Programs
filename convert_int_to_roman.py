class IntegerToRoman:
    def __init__(self):
        # Map of integer values to Roman numerals
        self.integer_to_roman_map = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

    def int_to_roman(self, num: int) -> str:
        """
        Convert an integer to a Roman numeral.

        Args:
            num (int): The integer to convert.

        Returns:
            str: The Roman numeral representation of the integer.
        """
        roman_numeral = ''  # Initialize the Roman numeral string
        # Iterate through the integer-to-Roman mapping in descending order of values
        for value, numeral in sorted(self.integer_to_roman_map.items(), reverse=True):
            # Append the corresponding Roman numeral while the number is greater than or equal to the value
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral


# Example usage:
converter = IntegerToRoman()
print(converter.int_to_roman(258))  # Output: CCLVIII
