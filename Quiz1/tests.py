# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:23:38 2017

@author: Ty
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
           L, list of unique positive integers sorted in descending order
    Use the greedy approach where you find the largest multiplier for 
    the largest value in L then for the second largest, and so on to 
    solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
    return: the sum of the multipliers or "no solution" if greedy approach does 
            not yield a set of multipliers such that the equation sums to 's'
    """
    tempSum = 0
    multSum = 0
    
    for num in L:
        mult = int((s-tempSum) / num)
        tempSum += mult*num
        multSum += mult
        
    if tempSum != s:
        return "no solution"
    else:
        return multSum
    
    


def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    return max_sum_rec(L, L[0], {})
    


def max_sum_rec(L, maxSum, sums):
    if sum(L) > maxSum:
        maxSum = sum(L)
    if len(L) < 2:
        return maxSum
    
    nextL = []
    for i in range(1, len(L)-1):
        nextL.append(L[i])
    if (nextL not in sums):
        sums[nextL] = max_sum_rec(nextL, maxSum, sums)
    if sums[nextL] > maxSum:
            maxSum = sums[nextL]
    nextL = []
    for i in range(len(L)-2):
        nextL.append(L[i])
    if (nextL not in sums):
        sums[nextL] = max_sum_rec(nextL, maxSum, sums)
    if sums[nextL] > maxSum:
            maxSum = sums[nextL]   
    
    
    return maxSum


print(max_contig_sum([3,4,-1,5,-4]))
    
    
    