class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            if (num not in dict1):
                dict1[num] = 1
            else:
                dict1[num] += 1 
        heap = []
        for num in dict1.keys():
            heapq.heappush(heap, (dict1[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        
        