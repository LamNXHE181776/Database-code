def spiralFill(n, m, arr):
    res = [[-1] * m for _ in range(n)]

    # Change in row index for each direction
    dr = [0, 1, 0, -1]

    # Change in column index for each direction
    dc = [1, 0, -1, 0]

    # Initial direction index (0 corresponds to 'right')
    dirIdx = 0

    index = 0
    r, c = 0, 0

    while index < len(arr):
        res[r][c] = arr[index]
        index += 1

        # The next cell indices
        newR = r + dr[dirIdx]
        newC = c + dc[dirIdx]

        # Check if the next cell is out of bounds or
        # it is already filled, then update the direction
        if newR < 0 or newR == n or newC < 0 or newC == m \
        						 or res[newR][newC] != -1:
            dirIdx = (dirIdx + 1) % 4

            newR = r + dr[dirIdx]
            newC = c + dc[dirIdx]

        # Update the cells
        r = newR
        c = newC

    return res


if __name__ == "__main__":
    m, n = 4, 4
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16]
    res = spiralFill(n, m, arr)

    for i in range(n):
        for j in range(m):
            print(res[i][j], end=" ")
        print()