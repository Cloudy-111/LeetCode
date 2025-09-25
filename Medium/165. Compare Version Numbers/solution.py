class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        separate_v1 = version1.split('.')
        separate_v2 = version2.split('.')

        min_len = min(len(separate_v1), len(separate_v2))
        i = 0
        while i < min_len:
            if int(separate_v1[i]) < int(separate_v2[i]):
                return -1
            elif int(separate_v1[i]) > int(separate_v2[i]):
                return 1
            i += 1

        if len(separate_v2) > len(separate_v1):
            while i < len(separate_v2):
                if int(separate_v2[i]) != 0:
                    return -1
                i += 1
        elif len(separate_v1) > len(separate_v2):
            while i < len(separate_v1):
                if int(separate_v1[i]) != 0:
                    return 1
                i += 1

        return 0
