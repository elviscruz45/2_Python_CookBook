nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
nums.sort()
print(nums)
import heapq
heap = list(nums)
heapq.heapify(heap)
print((heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
