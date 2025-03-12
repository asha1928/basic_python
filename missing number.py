def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  
    missing_number = expected_sum - actual_sum 
    return missing_number


n = 6  
arr = [1, 2, 3, 5, 6]  

missing_num = find_missing_number(arr, n)
print(f"The missing number is: {missing_num}")