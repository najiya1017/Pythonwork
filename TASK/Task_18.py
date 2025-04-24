def balancedStringSplit(s: str) -> int:
    balance = 0
    count = 0
    for char in s:
        if char == 'R':
            balance += 1
        elif char == 'L':
            balance -= 1
        if balance == 0:
            count += 1 
    return count
print(balancedStringSplit("RLRRLLRLRL"))  
print(balancedStringSplit("RLRRRLLRLL"))   
