from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        count = Counter(hand)
        print(count)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            k = minH[0]
            
            for i in range(k, k + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
