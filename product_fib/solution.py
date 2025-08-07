def longest_sequence(n):
    num_a, num_b = 0, 1

    while num_a * num_b < n:
        num_a, num_b = num_b, num_b + num_a

    if num_a * num_b == n:
        return {num_a, num_b}
    else:
        return {}

