#Amazon Fullfilment Builder
import heapq
def solve(l):
    heapq.heapify(l)
    ans=0
    while len(l)>1:
        a,b=heapq.heappop(l),heapq.heappop(l)
        ans+=a+b
        heapq.heappush(l,a+b)
    return ans
print solve([8,4,6,12])