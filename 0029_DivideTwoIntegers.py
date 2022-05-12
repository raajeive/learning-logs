class Solution:
    def divide(self, dividend, divisor):
        quotient = 0
        negativeFlag = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)   
        divisor = abs(divisor)
        this_sum = divisor
        while dividend >= this_sum:
            current_quotient = 1
            while (this_sum + this_sum) <= dividend:
                current_quotient += current_quotient
                this_sum += this_sum
            dividend -= this_sum
            this_sum = divisor
            quotient += current_quotient
        return min(2147483647, max(quotient if not negativeFlag else -quotient, -2147483648))
