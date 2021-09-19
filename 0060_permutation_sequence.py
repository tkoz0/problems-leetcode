class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        while len(factorial) < 10:
            factorial.append(len(factorial)*factorial[-1])
        index = k-1
        numbers = [str(i) for i in range(1,n+1)]
        result = ''
        while numbers:
            f = factorial[len(numbers)-1]
            choice = index//f
            result += numbers.pop(choice)
            index -= choice*f
        return result
