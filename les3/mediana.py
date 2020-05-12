class MedianFinder:

    def __init__(self, data = None):
        """
        initialize your data structure here.
        """
        if data == None:
            self._list  = []
        else:
            self._list = data

    def addNum(self, num: int) -> None:
        self._list.append(num)

    def findMedian(self) -> float:
        sorted_lst = sorted(self._list)
        _len = len(self._list)
        if (_len % 2 == 1):
            return sorted_lst[_len//2]
        else:
            return ( (sorted_lst[_len//2 - 1] +
                sorted_lst[_len//2 ]) ) //2

m=MedianFinder([9,5,7])
print(m._list)
print(m.findMedian())
m.addNum(42)
print(m._list)
print(m.findMedian())
