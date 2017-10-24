###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowList = []
    for cow in cows:
        cowList.append(cow)
    cowList.sort(key=lambda cow: 1/cows[cow])
    trips = []
    wLeft = limit
    currentTrip = []
    #main trip loop
    while (len(cowList) > 0):
        i = 0
        noCow = False
        while (cows[cowList[i]] > wLeft):
            i += 1
            if (i >= len(cowList)):
                #finsih current trip
                trips.append(currentTrip)
                currentTrip = []
                wLeft = limit
                noCow = True
                break
        #now i is largest cow that can fit
        if (not noCow):
            currentTrip.append(cowList[i])
            wLeft -= cows[cowList[i]]
            del cowList[i]

    if (currentTrip != []):
        trips.append(currentTrip)
    return trips
        

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best = []
    for cow in cows:
        best.append([cow])
    for part in get_partitions(cows):
        valid = True
        for trip in part:
            sum = 0
            for cow in trip:
                sum += cows[cow]
            if sum > limit:
                valid = False
        if (valid and len(part) < len(best)):
            best = part
    return best
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    print("for greedy")
    

    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    print("for brute")

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

#print(greedy_cow_transport(cows, limit))
#print(greedy_cow_transport({'Muscles': 65, 'Polaris': 20, 'Patches': 60, 'Milkshake': 75, 'MooMoo': 85, 'Lotus': 10, 'Clover': 5, 'Louis': 45, 'Horns': 50, 'Miss Bella': 15}, 100))
#print(greedy_cow_transport({'Daisy': 50, 'Betsy': 65, 'Coco': 10, 'Dottie': 85, 'Lilly': 24, 'Abby': 38, 'Buttercup': 72, 'Rose': 50, 'Patches': 12, 'Willow': 35}, 100))
#print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()


