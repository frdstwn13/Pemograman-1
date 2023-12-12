def ops(n, A, B):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = 0
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def main():
    n = int(input())

    A = []
    print("Matriks A:")
    for _ in range(n):
        row = list(map(int, input().split()))
        A.append(row)

    B = []
    print("Matriks B:")
    for _ in range(n):
        row = list(map(int, input().split()))
        B.append(row)

    result = ops(n, A, B)

    print("Matriks AXB:")
    for row in result:
        for element in row:
            print(element, end=" ")
        print()

if __name__ == "__main__":
    main()