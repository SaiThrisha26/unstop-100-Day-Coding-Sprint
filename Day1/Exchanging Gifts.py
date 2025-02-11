def find_youngest_member(n, m, gift_data):
    # Initialize in-degree and out-degree arrays
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    # Process the gift data
    for a, b in gift_data:
        out_degree[a] += 1
        in_degree[b] += 1

    # Identify the youngest member
    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i

    # If no such member exists
    return -1


# Input handling
if __name__ == "__main__":
    n, m = map(int, input().split())
    gift_data = [tuple(map(int, input().split())) for _ in range(m)]
    print(find_youngest_member(n, m, gift_data))
