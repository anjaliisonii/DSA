'''Problem Description :
The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.'''

def calculate (r, unit, arr, n):
    if n == 0:
        return -1 
        
    totalFoodRequired = r * unit 
    foodTillNow = 0 
    house = 0 
        
    for house in range (n):
        foodTillNow += arr[house] 
        if foodTillNow>=totalFoodRequired:
            break 
    if totalFoodRequired > foodTillNow:
        return 0
    return house + 1
	  
r = int (input ())
unit = int (input ())
n = int (input ())
  
arr = list (map (int, input ().split ()))
print (calculate (r, unit, arr, n))
