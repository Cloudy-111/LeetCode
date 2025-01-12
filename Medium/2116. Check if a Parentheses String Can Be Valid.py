class Solution:
    # Mấu chốt của bài toán là cách tạo ra xâu ngoặc hợp lệ là với mỗi dấu ) thì phải có dấu ( tương ứng trước nó (không cần tính liên tiếp)-> nút gỡ bài toán
    # Trong đề bài, có kí tự với chỉ số locked là 0 thì sẽ được thay đổi giữa ( và )
    # Như vậy khi duyệt xâu, khi gặp đến kí tự ) mà bị khóa thì ta cần tìm xem có kí tự ( nào trước đó cũng bị khóa không
    # Nếu không còn kí tự ( bị khóa thì ta tìm đến kí tự không bị khóa, bởi vì nó có thể biến thành ( hay )
    # Nên ưu tiên chọn kí tự ( bị khóa trước kí tự không bị khóa vì nếu mà chọn trước thì sẽ bị phí đi 1 lần dùng phần tử để thay đổi kí tự
    # Như vậy, ta dùng stack để lưu các vị trí của kí tự ( bị khóa và những vị trí của các kí tự không bị khóa
    # Nếu đã duyệt hết rồi mà vẫn còn dấu ( bị khóa và kí tự không bị khóa thì ta ghép cặp nó
    # Nếu vẫn còn dư dấu ( bị khóa thì không hợp lệ
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        open_parenthsis = []
        unlocked = []
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                open_parenthsis.append(i)
            elif s[i] == ')':
                if len(open_parenthsis) > 0:
                    open_parenthsis.pop()
                elif len(unlocked) > 0:
                    unlocked.pop()
                else:
                    return False
        while open_parenthsis and unlocked and open_parenthsis[-1] < unlocked[-1]:
            open_parenthsis.pop()
            unlocked.pop()
        if open_parenthsis:
            return False
        return True
