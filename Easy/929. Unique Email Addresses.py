class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        def standardEmail(email):
            name = email.split('@')
            local = name[0]
            domain = name[1]
            if '+' in local:
                local = local[:local.index('+')]
            local = ''.join(local.split('.'))
            return local + '@' + domain
        for i in emails:
            s.add(standardEmail(i))
        print(s)
        return len(s)
