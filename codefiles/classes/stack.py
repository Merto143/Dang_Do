from typing import Any, Callable


class Stack:

    def __init__(self) -> None:
        """post: creates an empty LIFO list"""
        self.stack: list[Any] = []

    def push(self, item: Any) -> None:
        """post: puts x at top of the stack"""
        self.stack.append(item)

    def pop(self) -> Any:
        """
        pre: Non-empty stack
        post: Removes last/top item of the stack
        """
        self.stack.pop()

    def top(self) -> Any:
        """
        pre: Non-empty stack
        post: Shows next item in the stack to be popped
        """
        return self.stack[-1]

    def size(self) -> int:
        """ post: returns length of the stack """
        return len(self.stack)

    def __repr__(self) -> str:
        """ post: represents how an instance is printed """
        return f"{self.stack}"
