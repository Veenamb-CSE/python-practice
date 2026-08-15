class Solution:
    def average(self, salary: List[int]) -> float:
        count=len(salary)
        count=count-2
        x=max(salary)
        y=min(salary)
        sum=x+y
        avg=0.0
        for i in range(0,len(salary)):
            avg+=salary[i]
        avg=(avg-sum)/count
        return avg
        
