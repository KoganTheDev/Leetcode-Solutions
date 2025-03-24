class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = [0] * (n - k + 1)
        counter = Counter(nums[:k])
        
        answer[0] = self.get_sum(counter, x)

        for i in range(1, n - k + 1):
            tail_idx = i - 1
            tail = nums[tail_idx]
            head_idx = k + tail_idx
            head = nums[head_idx]

            if head == tail:
                answer[i] = answer[i - 1]
                continue

            if counter[tail] == 1:
                del counter[tail]
            else:
                counter[tail] -= 1

            counter[head] += 1
            
            answer[i] = self.get_sum(counter, x)

        return answer

    def get_sum(self, counter: Counter, x: int) -> int:
        pq = [(count, num) for num, count in counter.items()]
        heapq.heapify(pq)
        
        sum_value = sum(num * count for num, count in counter.items())

        while len(pq) > x:
            count, num = heapq.heappop(pq)
            sum_value -= num * count

        return sum_value