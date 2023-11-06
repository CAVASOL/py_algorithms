class MyHashMap:

    def __init__(self):
        self.values = [-1] * (10**6+1)

    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        return self.values[key]

    def remove(self, key: int) -> None:
        self.values[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# class MyHashMap:
#     def __init__(self):
#         self.size = 1000  # Choose an appropriate initial size
#         self.buckets = [None] * self.size

#     def put(self, key, value):
#         index = key % self.size
#         if self.buckets[index] is None:
#             self.buckets[index] = [(key, value)]
#         else:
#             for i, (existing_key, existing_value) in enumerate(self.buckets[index]):
#                 if existing_key == key:
#                     self.buckets[index][i] = (key, value)
#                     return
#             self.buckets[index].append((key, value))

#     def get(self, key):
#         index = key % self.size
#         if self.buckets[index] is not None:
#             for existing_key, existing_value in self.buckets[index]:
#                 if existing_key == key:
#                     return existing_value
#         return -1

#     def remove(self, key):
#         index = key % self.size
#         if self.buckets[index] is not None:
#             for i, (existing_key, existing_value) in enumerate(self.buckets[index]):
#                 if existing_key == key:
#                     del self.buckets[index][i]
#                     return

# myHashMap = MyHashMap()
# myHashMap.put(1, 1)
# myHashMap.put(2, 2)
# print(myHashMap.get(1))  # Output: 1
# print(myHashMap.get(3))  # Output: -1
# myHashMap.put(2, 1)      # Update the existing value
# print(myHashMap.get(2))  # Output: 1
# myHashMap.remove(2)      # Remove the key 2
# print(myHashMap.get(2))  # Output: -1