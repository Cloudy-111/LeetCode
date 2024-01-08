class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        dic = {}
        for i, j in enumerate(months):
            dic[j] = str(i + 1)
        day = date.split()
        res = []
        y = int(day[-1])
        m = int(dic[day[-2]])
        d = int(day[0][:len(day[0]) // 2])
        res.append(f'{y:04d}')
        res.append(f'{m:02d}')
        res.append(f'{d:02d}')
        return '-'.join(res)
