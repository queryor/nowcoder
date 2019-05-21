'''There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
'''
# 假设开始设置起点start = 0, 并从这里出发，如果当前的gas值大于cost值，就可以继续前进，此时到下一个站点，
# 剩余的gas加上当前的gas再减去cost，看是否大于0，若大于0，则继续前进。
# 当到达某一站点时，若这个值小于0了，则说明从起点到这个点中间的任何一个点都不能作为起点，则把起点设为下一个点，继续遍历
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        ### 最朴素的搜索 o(n^2) 超时
        n = len(gas)
        for s in range(n):
            flag = False
            tank = gas[s]-cost[s]
            cur = (s+1)%n
            while tank>=0:
                if cur == s:
                    flag = True
                    break
                tank = tank + gas[cur]-cost[cur]
                cur = (cur+1)%n
            if flag == True:
                return s
        return -1

    def canCompleteCircuit1(self, gas, cost) -> int:
        n = len(gas)
        total = 0
        tank = 0
        start = 0
        for i in range(n):
            total+=gas[i]-cost[i]
            tank += gas[i]-cost[i]
            if tank<0:
                start = i+1
                tank = 0
        return start if total>=0 else -1
        
        


s = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit1(gas,cost))
