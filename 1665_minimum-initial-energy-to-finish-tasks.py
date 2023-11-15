class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks,key=lambda x:-(x[1]-x[0]))
        e = 0
        spent = 0
        for a,m in tasks:
            if e - spent < m:
                e = spent + m
            spent += a
        return e
