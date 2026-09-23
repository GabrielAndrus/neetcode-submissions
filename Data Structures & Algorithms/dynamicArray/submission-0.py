class DynamicArray:
    capacity: int
    length: int
    arr: List

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1
    
    def popback(self) -> int:
        final_element = self.arr[self.length - 1] # Get final element
        self.arr[self.length-1] = None
        self.length -= 1
        return final_element

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = self.capacity * [0]
        for i in range(0, len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
