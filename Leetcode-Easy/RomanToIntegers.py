class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

        # Initialize result
        sum = 0
        i = 0
        while i < len(s):
            # If the current value is less than the next
            # value, subtract current from next and add to sum
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                sum += roman_map[s[i + 1]] - roman_map[s[i]]
                # Skip the next symbol
                i += 2
            else:
                # Otherwise, add the current value to sum
                sum += roman_map[s[i]]
                i += 1

        return sum
            
        
