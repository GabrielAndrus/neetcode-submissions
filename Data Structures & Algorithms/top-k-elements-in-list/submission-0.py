class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Intialize a frequency list
        freq = [[] for i in range(0, len(nums) + 1)]
        # initialize a hash map to store frequency
        count = {}

        # Get the counts of each num and store in count at index num
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # update to frequency list -- count is sorted luckily
        for num, count in count.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result