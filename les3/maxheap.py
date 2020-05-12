class MaxHeap:
    def __init__(self, items = []) -> None:
        self.heap = []
        self.heapify(items)

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def pop(self) -> int:
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(0)
        elif len(self.heap) == 1:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def heapify(self, items) -> None:
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap)-1)

m = MaxHeap([95,3,21])
print(m.heap)
m.push(10)
print(m.heap)
m.push(22)
print(m.heap)
print(m.pop())
print(m.heap)
print(m.peek())
print(m.heap)
