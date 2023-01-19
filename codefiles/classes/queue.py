from typing import List, Any

class Queue:

    def __init__(self) -> None:
        """post: creates an empty FIFO queue"""
        self.list: List[Any] = []

    def enqueue(self, x: Any) -> None:
        """post: adds x at back of queue"""
        self.list.append(x)

    def dequeue(self) -> Any:
        """pre: self.size() > 0
                post : removes and returns the front item"""
        if self.size() > 0:
            return self.list.pop(0)
        else:
            print("No objects in queue")

    def front(self) -> Any:
        """pre: self.size() > 0
                postcondition: returns first item in queue"""
        if self.size() > 0:
            return self.list[0]
        else:
            print("No objects in queue")

    def size(self) -> int:
        """postcondition: return number of items in queue"""
        return len(self.list)
