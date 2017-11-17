#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:19:34 2017

@author: tymarking
"""
import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    results = []
    for trial in range(numTrials):
        bucket = [0,0,0,1,1,1]
        for i in range(3):
            index = random.randrange(0,len(bucket))
            if bucket[index] == 1:
                results.append(0)
                break
            else:
                del bucket[index]
            if i == 2:
                results.append(1)
    
    return 2*sum(results)/(float)(len(results))
        


print(noReplacementSimulation(30000))