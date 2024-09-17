import sys

def power_modulo(m, k, n):
    '''   
    #Unoptimised
    y = 0
    
    if(k==1):
        return m % n
    
    else:
        y = m % n
        y = (y * power_modulo(m, k-1, n)) %n
        print (y)
        
    return y
    '''   

#Optimised

    if (k == 0):
        return 1
     
    # If k is Even
    y = 0
    if (k % 2 == 0):
        y = power_modulo(m, k / 2, n)
        y = (y * y) % n
         # If k is Odd
    else:
        y = m % n
        y = (y * power_modulo(m, k - 1, n) % n) % n
            
    return ((y + n) % n)

try:
    num_line = int(sys.stdin.readline())
    
    for _ in range(num_line):
        a = [int(s) for s in sys.stdin.readline().split()]
        m, k, n = a[0], a[1], a[2]
        print(power_modulo(m, k, n))
except:
    print("numbers are not integers")
    

'''
Base Case
When ( k = 0 ), the function returns 1, therefore a constant-time operation, O(1).

Recursive Case
When ( k ) is not zero, the function makes recursive calls. Let’s break it down:

If ( k ) is even:
The function calls itself with ( k / 2 ).
This reduces the problem size by half.
The time complexity for this case is (T(k/2) .

If ( k ) is odd:
The function calls itself with ( k - 1 ).
This reduces the problem size by 1.
The time complexity for this case is  T(k-1) .

Time Complexity Analysis
To find the overall time complexity, we consider the worst-case scenario

The key observation here is that the function reduces the exponent ( k ) by half in each recursive call when ( k ) is even. 
This results in a logarithmic reduction of the problem size.

Let’s denote the time complexity of the function as ( T(k) ).

For even ( k ): [ T(k) = T(k/2) + O(1) ]

For odd ( k ): [ T(k) = T(k-1) + O(1) ]

However, the dominant term is when ( k ) is even because it reduces the problem size more significantly. Therefore, we can approximate the time complexity as:

[ T(k) \approx T(k/2) + O(1) ]

This recurrence relation can be solved using the Master Theorem for divide-and-conquer recurrences. The solution to this recurrence relation is:

[ T(k) = O(\log k) ]

'''