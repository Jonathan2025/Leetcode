# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique







class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        # our first case is IF the gas is <= cost then that means we are not able to make a full trip and therefore there is not solution
        if sum(gas) < sum(cost):
            return -1


        # now if we pass here that means we will have a solution.
        # initialize our variables. Total of differences and the starting position
        total = 0
        starting = 0 


        for i in range(len(gas)):
            total += gas[i] - cost[i] # we add the differences to the total 
            # if the total ever hits below 0 then that means we need to restart at a new starting position and reset the total
            if total < 0: 
                total = 0 
                starting = i + 1 # start at the next position


        return starting