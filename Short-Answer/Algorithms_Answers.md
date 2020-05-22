#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the loop will start at 0 and continue up until n essentially. It will, in reality go until n^3 but a is not just increasing by 1 each time. It is increasing by n^2. 


b) O(nlogn) because the for loop will iterate over every element in n, but the inner while loop is incrementing itself by twice its previous value each time, so it will not take O(n) to complete that loop


c) O(n) because the time it takes to complete this function will increase with input size. If the input is 1 it will take less time to reach the base case of 0. If the input size is 1000, it will take much longer since we are adding 2 then subtracting one with each recursive loop

## Exercise II


2 highest floor

U - understand
    inputs and outputs
    input - number of floors, and 'plenty' of eggs
    output - f, the floor below which eggs do not break

    n represents the total number of floors, while f is some number from 1 to n which is the floor below which eggs will break

    this function is meant to optimize a process which would otherwise be linearly going to each floor and dropping eggs until we discover the correct floor

P - Plan
    tools
    binary search - this problem lends itself to binary search because eggs will not break on a floor lower than f. So if eggs not breaking, f must be a higher-numbered floor and we don't need to search any lower floors. We can eliminate half of the floors each time.


E - Execute (in pseudocode)

    define a function which takes as parameters n floors
        initialize a variable to hold the starting point for our search
            this will be set to the first floor
        initialize a variable to hold the ending point for our search
            this will be set to the top floor
        
        create a loop which will continue as long as our starting and ending points have not crossed over each other
            define a midpoint between the current starting and ending values
            if at the current floor eggs break, but at the floor below, they do not, we have found f and can return this floor number
            if at the current floor eggs are not breaking, set the new start to be the former midpoint (plus one so we don't search the actual midpoint again) and the end stays the same. Continue searching.
            if at the current floor eggs break, but at the floor below, they also break, we need to keep searching, but floor 'f' is below. Set the end to be the former midpoint -1 and continue searching.