def find_flower_indices(n, t, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Total types of flowers
        t (int): Total number of flowers needed
        arr (list): List of integers representing types of flowers
    Returns:
        tuple: A tuple with two integers representing the indices of the two flowers
    """
    m=0
    while m<n:
        s=arr[m]
        for i in range(m+1,n):
            if s+arr[i] ==t:
                return m,i
        m=m+1
        
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    t = int(data[1])  # Second input is the integer t
    arr = list(map(int, data[2:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = find_flower_indices(n, t, arr)
    
    # Print the output in the required format
    print(result[0], result[1])

if __name__ == "__main__":
    main()
