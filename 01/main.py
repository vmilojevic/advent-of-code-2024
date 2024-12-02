def total_distance(left, right):
    left.sort()
    right.sort()

    result = 0
    for l, r in zip(left, right):
        result = result + abs(l - r)
    
    return result

def similarity_score(left, right):
    right_map = {}

    for r in right:
        right_map[r] = right_map.get(r, 0) + 1
    
    result = 0
    for l in left:
        result = result + l * right_map.get(l, 0)
    
    return result

if __name__ == "__main__":
    left = []
    right = []

    input = open("input.txt")
    for line in input:
        split_line = line.split()
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))
    
    print("Total distance: " + str(total_distance(left, right)))
    print("Similarity score: " + str(similarity_score(left, right)))
    