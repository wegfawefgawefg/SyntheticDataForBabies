def circular_distance(num_divisions, a, b):
    diff = abs(a - b)
    half = num_divisions / 2
    if diff > half:
        diff = half - abs(diff - half)
    return diff

if __name__ == "__main__":
    #   hours
    print(circular_distance(24, 6, 0))
    print(circular_distance(24, 12, 0))

    #   days
    print(circular_distance(7, 0, 5))