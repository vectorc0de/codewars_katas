def longest_sequence(n):
    longest = []
    for i in range(1, int(n**0.5) + 1):
        total = 0
        current_sequence = []        
        j = i

        while total + j**2 <= n:
            total += j**2
            current_sequence.append(j)
            
            if total == n:
                if len(current_sequence) > len(longest):
                    longest = current_sequence
                break
            
            j += 1
            
    return longest if longest else None