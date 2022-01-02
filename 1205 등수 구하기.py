N, score, P = map(int, input().split())

if N > 0:
    score_list = list(map(int, input().split()))
    if N == P and score <= score_list[-1]:
        print(-1)
    else:
        idx = N+1
        for i in range(N):
            if score_list[i] <= score:
                idx = i+1
                break
        print(idx)
else:
    print(1)