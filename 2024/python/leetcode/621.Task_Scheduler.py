class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        ret = 0

        while 1:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                ret += 1

                counter.subtract(task)
                # 0 이하인 아이템 제거
                counter += collections.Counter()  # 빈 Counter 더하면 0 이하인 아이템 제거됨

            if not counter:
                break

            ret += n - sub_count + 1
        return ret