N, M = map(int, input().split())

s = []

def f() :
    if len(s) == M :
        print(" ".join(map(str, s)))
        return

    for i in range(1, N+1) :
        if len(s) == 0 or i >= s[-1] :
            s.append(i)
            f()
            del s[-1]

f()