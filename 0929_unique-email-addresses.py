class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret = set()
        for email in emails:
            local,domain = email.split('@')
            local = local.replace('.','')
            if '+' in local:
                local = local[:local.find('+')]
            ret.add(f'{local}@{domain}')
        print(ret)
        return len(ret)
