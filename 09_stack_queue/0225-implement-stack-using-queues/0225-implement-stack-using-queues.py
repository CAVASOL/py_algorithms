class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft() if self.q1 else None

    def top(self) -> int:
        return self.q1[0] if self.q1 else None

    def empty(self) -> bool:
        return not self.q1 and not self.q2

# class MyStack:

#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, x: int) -> None:
#         if not self.q1 and not self.q2:
#             self.q1.append(x)
#             return

#         if self.q1:
#             self.q2.append(x)
#             while self.q1:
#                 self.q2.append(self.q1.popleft())
#         else:
#             self.q1.append(x)
#             while self.q2:
#                 self.q1.append(self.q2.popleft())

#     def pop(self) -> int:
#         if self.q1:
#             return self.q1.popleft()
#         elif self.q2:
#             return self.q2.popleft()
#         else:
#             return None

#     def top(self) -> int:
#         if self.q1:
#             return self.q1[0]
#         elif self.q2:
#             return self.q2[0]
#         else:
#             return None

#     def empty(self) -> bool:
#         return not self.q1 and not self.q2