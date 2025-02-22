class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp + temp:  # Exponential subtraction
                temp += temp
                multiple += multiple
            
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient

            

        