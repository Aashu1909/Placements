import heapq

pq = [5, 20, 1, 30, 4]

heapq.heapify(pq)  # [1,4,5,30,20]
print(pq)

heapq.heappush(pq, 3)  # 1,4,3,30,20,5
print(pq)

print(heapq.heappop(pq))  # [3,4,5,30,20]
print(pq)

print(heapq.nlargest(2, pq))

print(heapq.nsmallest(2, pq))


pq = [5, 20, 1, 30, 4]

heapq.heapify(pq)  # [1,4,5,30,20]
print(pq)

print(heapq.heappushpop(pq,2))
print(pq)

print(heapq.heappushpop(pq,0))
print(pq)

print(heapq.heapreplace(pq,-1))
print(pq)