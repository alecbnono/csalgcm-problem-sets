def condition(e):
    return e[0] - e[1]


def query(movies, s, e, a, k):

    range = movies[s:e+1]

    if a < k or not range:
        return -1
    else:
        # length of last movie
        lastMovie = 0

        while a >= k and range:

            lastMovie = max(range, key=condition)
            range.pop(range.index(lastMovie))
            a -= k

        return lastMovie[0] - lastMovie[1]


n = int(input())
movies = []
for i in range(n):
    r, c = list(map(int, input().rstrip().split(" ")))
    movies.append([r, c])

q = int(input())
for cc in range(q):
    s, e, a, k = list(map(int, input().rstrip().split(" ")))
    print(query(movies, s, e, a, k))
    # solve for answer here
