class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        huns = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        thos = ['','M','MM','MMM']
        digits = []
        while num:
            digits.append(num%10)
            num //= 10
        result = ones[digits[0]]
        if len(digits) >= 2:
            result = tens[digits[1]] + result
        if len(digits) >= 3:
            result = huns[digits[2]] + result
        if len(digits) == 4:
            result = thos[digits[3]] + result
        return result
