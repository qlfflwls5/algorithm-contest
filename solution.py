# 별 헤는 밤
# 쉬이 잠들지 못한 새벽, 윤동주 시인은 창 앞에 고요히 앉아 밖을 바라봤다.
# 밤하늘을 수놓은 별들을 보며 지독한 그리움에 감싸인 윤동주 시인은 '별 헤는 밤'을 써 내려가기 시작했다.

#  "별 하나에 추억과
#    별 하나에 사랑과
#    별 하나에 쓸쓸함과
#    별 하나에 동경과
#    별 하나에 시와
#    별 하나에 어머니, 어머니..."

# 별빛이 내린 아름다운 밤을 오래도록 바라보다 윤동주 시인은 문득 별들을 잇는 별자리를 헤아리고 싶었다.
# '별자리는 어떻게 이어지는 걸까'
# 윤동주 시인은 별빛과 별빛이 겹치는 별들을 하나의 별자리로 세어 나갔다.
# 그는 눈에 들어온 별자리들의 수와 가장 많은 별로 이루어진 별자리의 크기를 알고 싶었다.

# 윤동주 시인이 '별 헤는 밤'을 완성할 수 있도록 별자리에 대한 정보를 알아내는 프로그램을 작성하라.


# [예시]
# 각각의 별은 자신의 위치에서 밝기에 맞는 정사각형 마름모의 형태로 빛을 내뿜는다. 밤하늘을 벗어나는 빛은 표현하지 않는다.
# 이때, 밝기 범위가 겹치는 별들끼리는 하나의 별자리로 본다.
# 또한, 아무 별과 이어지지 않은 별도 하나의 별자리로 본다.

# 위 그림은 행, 열, 밝기가 각각 (4, 4, 3), (6, 6, 4), (8, 2, 2)인 별들을 밤하늘에 나타낸 모습이다.
# 밝기가 3인 별과 밝기가 4인 별의 밝기 범위가 겹치므로 둘은 하나의 별자리를 이룬다.
# 밝기가 2인 별은 어떠한 별과도 밝기 범위가 겹치지 않으므로 혼자 하나의 별자리를 이룬다.
# 따라서, 위 그림의 경우 총 2개의 별자리가 존재한다.

# 한편, 별자리의 크기는 다음과 같은 과정을 통해 구한다.

# 1. 별자리를 이루고 있는 별들의 모든 쌍의 각 거리의 제곱을 구한다. 이 거리의 제곱은 편의상 별 한 쌍을 연결하는 간선의 길이로 본다.
# 2. 모든 별을 연결하는 간선들의 가능한 길이의 합 중 최솟값을 별자리의 크기로 한다.


# 위 그림은 (4, 4, 3), (6, 6, 4), (9, 4, 3), (8, 8, 2)의 정보를 갖는 별들이 한 별자리를 이루고 있을 때 가능한 간선의 유형 중 두 가지 예시다.
# 왼쪽 예시의 경우 간선의 길이 총합은 25 + 17 + 8 = 50이다.
# 오른쪽 예시의 경우 간선의 길이 총합은 13 + 8 + 8 = 29이다.
# 두 예시 모두 모든 별을 연결하지만, 오른쪽 예시가 간선의 길이의 합이 최소가 되는 '별자리의 크기'가 된다.


# [제약 사항]
# 밤하늘은 한 변의 길이가 N인 정사각형이다.(5 <= N <= 20)
# 밤하늘의 별의 개수 M은 1 ~ 50이다.
# 행과 열은 각각 0 ~ N-1이다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 세 자연수 N, M가 주어진다.
# N은 윤동주 시인이 보는 정사각형 밤하늘의 한 변의 길이, M은 별의 개수이다.
# 다음 M개의 줄에는 각 별의 행, 열, 밝기가 공백으로 구분되어 주어진다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 총 별자리의 개수와 가장 많은 별로 이루어진 별자리의 크기를 공백으로 구분해 출력하라.


# dfs를 통한 상호배타집합의 Union Set과정 구현
def dfs(s, cur_star):
    visited = [0]*M
    visited[s] = 1
    stack = [s]
    while stack:
        v = stack.pop()
        p_cnt[v] = cur_star
        for w in AL[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = 1


def find_set(x):
    if x != p_size[x]:
        x = p_size[x]

    return x


def kruskal():
    S = 0
    cnt = 0
    for s, e, w in edges:
        rep_s, rep_e = find_set(s), find_set(e)
        if rep_s != rep_e:
            p_size[rep_e] = rep_s
            S += w
            cnt += 1
            # (Kruskal을 적용할 집합의 원소 개수 -1)개의 간선이 채워지면 종료
            if cnt == max(star_cnt) - 1:
                break

    return S


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    stars = []
    for _ in range(M):
        stars.append(tuple(map(int, input().split())))

    sky = [[0]*N for _ in range(N)]
    # 상호배타집합 p_cnt 생성
    p_cnt = [i for i in range(M)]
    AL = [set() for _ in range(M)]
    # 별자리 개수 구하기
    # 입력을 받는 순서대로 N*N 크기의 격자판에 행(r), 열(c), 밝기(l)를 이용하여 정사각형 마름모 형태로 별의 밝기 범위를 표시
    for i in range(M):
        star = stars[i]
        r, c, l = star
        for j in range(l):
            for nc in range(c-j, c+j+1):
                if 0 <= r-l+j+1 < N and 0 <= nc < N:
                    # 이미 다른 별의 밝기 범위가 표시되어 있는 경우 p_cnt와 dfs를 이용하여 현재 별을 기존에 차지하고 있던 별과 연결
                    if sky[r-l+j+1][nc]:
                        pre_star = sky[r-l+j+1][nc] - 1
                        dfs(pre_star, i)
                        AL[i].add(pre_star)
                        AL[pre_star].add(i)
                    sky[r-l+j+1][nc] = i + 1
                if 0 <= r+l-j-1 < N and 0 <= nc < N:
                    if sky[r+l-j-1][nc]:
                        pre_star = sky[r+l-j-1][nc] - 1
                        dfs(pre_star, i)
                        AL[i].add(pre_star)
                        AL[pre_star].add(i)
                    sky[r+l-j-1][nc] = i + 1

    # 별자리 크기 구하기
    edges = []
    star_cnt = [p_cnt.count(i) for i in range(M)]
    max_star = star_cnt.index(max(star_cnt))
    # 시작 별(s), 끝 별(e), 별 간의 거리(w) 정보를 갖는 모든 별 쌍의 간선을 구해 edges에 append
    for i in range(M-1):
        for j in range(i+1, M):
            if p_cnt[i] == max_star and p_cnt[j] == max_star:
                distance = (stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2
                edges.append((i, j, distance))
    # Kruskal 알고리즘을 사용하기 위해서 edges를 별 간의 거리(w)를 기준으로 오름차순 정렬
    edges = sorted(edges, key=lambda x: x[2])
    # Kruskal 알고리즘을 위한 상호배타집합 p_size 생성(가장 많은 별을 가진 별자리 내에서의 상호배타집합)
    p_size = [i for i in range(M)]
    size = kruskal()

    print('#%d %d %d' % (t, len(set(p_cnt)), size))
