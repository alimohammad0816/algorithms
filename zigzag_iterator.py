"""
ZigZagIterator
[1, 3, 5, 7, 9], [2, 4, 6, 8, 10] ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


class ZigZag:
    def __init__(self, list_1: list, list_2: list):
        self.list = [list_1, list_2]
    
    def next(self):
        v = self.list.pop(0)
        r = v.pop(0)
        if v:
            self.list.append(v)

        return r
    
    def has_next(self):
        if self.list:
            return True
        else:
            return False


z = ZigZag([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
while z.has_next():
    print(z.next())
