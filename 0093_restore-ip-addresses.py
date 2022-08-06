class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        def recur(digits,dots,ip):
            nonlocal ret
            if dots == 0:
                if len(digits) == 0:
                    return
                if len(digits) > 1 and digits[0] == '0':
                    return
                if int(digits) < 256:
                    ret.append(ip+digits)
            else:
                for i in range(1,len(digits)):
                    num = digits[:i]
                    if int(num) >= 256 or (len(num) > 1 and num[0] == '0'):
                        break
                    recur(digits[i:],dots-1,ip+num+'.')
        recur(s,3,'')
        return ret
