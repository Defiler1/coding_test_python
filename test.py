def greedy_coins():
   n = 1260 
   total_coin = 0

   coin_list = [500, 100, 50, 10]

   for coin in coin_list:
      total_coin += n // coin
      n = n % coin

   print(total_coin)


def big_number():
   n, m, k = map(int, input().split())
   num_list = list(map(int, input().split()))
   num_list.sort()
   num_list.reverse()
   first = num_list[0]
   second = num_list[1]
   result = 0

   while m != 0:
      for i in range(k):
         result += first
         m -= 1
      result += second
      m -= 1

   print(result)


def big_number2():
   n, m, k = map(int, input().split())
   num_list = list(map(int, input().split()))
   num_list.sort()
   num_list.reverse()
   first = num_list[0]
   second = num_list[1]
   result = 0
   count = int(m / (k + 1)) * k
   count += m % (k + 1)

   result += count * first
   result += (m - count) * second

   print(result)


def num_card_game():
   n, m = map(int, input().split())
   card_list =[]
   for _ in range(n):
      num_list = list(map(int, input().split()))
      card_list.append(min(num_list))

   print(max(card_list))


def to_1():
   n, k = map(int, input().split())
   result = 0
   while n != 1:
      if n / k > 0:
         if n % k == 0:
            n /= k
            result += 1
      n -= 1
      result += 1

   print(result)


def LRUD():
   n = int(input())
   plans = list(input().split())
   # R R R U D D
   x, y = 1, 1

   dx = [0, 0, -1, 1]
   dy = [-1, 1, 0, 0]
   move_types = ['L', 'R', 'U', 'D']

   for plan in plans:
      for i in range(len(move_types)):
         if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
      if nx < 1 or ny < 1 or nx > n or ny > n:
         continue

      x, y = nx, ny

   print(x, y)


def time_count():
   n = int(input())

   count = 0

   # 0 ~ n+1
   for i in range(n + 1):
      # 0 ~ 59
      for j in range(60):
         # 0 ~ 59
         for k in range(60):
            if '3' in str(i) + str(j) + str(k):
               count += 1

   print(count)

def kinght_move():
   init_location = input()
   row = init_location[1]
   column = int(ord(init_location[0])) - int(ord('a')) + 1
   steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
   
   result = 0
   
   for step in steps:
      nrow = row + step[0]
      ncolumn = column + step[1]
      if nrow >= 1 and nrow <= 8 and ncolumn >= 1 and ncolumn <= 8:
         result += 1
   
   print(result)


# n * (n - 1)!
def factorial(n):
   if n <= 1:
      return 1
   return n * factorial(n -1)

# print(factorial(5))


# 5-6.py 인접 행렬 방식 예제
# INF = 99999999999

# 리스트를 이용해 인접 행렬 표현
# graph = [
#    [0,7,5],
#    [7,0,INF],
#    [5,INF,0]
# ]


# 인접 리스트 표현
# graph = [[] for _ in range(3)]


# graph[0].append((1,7))
# graph[0].append((2,5))

# graph[1].append((0,7))

# graph[2].append((0,5))

# print(graph)


# 5-8.py DFS 메서드 정의
def dfs(graph, v, visited):
   # 현재노드 방문처리
   visited[v] = True
   print(v, end=' ')
   # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
   for i in graph[v]:
      if not visited[i]:
         dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph= [
   [],
   [2,3,8],
   [1,7],
   [1,4,5],
   [3,5],
   [3,4],
   [7],
   [2,6,8],
   [1,7],
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# dfs(graph, 1, visited)


# 5-9.py BFS 메서드 정의
from collections import deque

def bfs(graph, start, visited):
   # 큐(Queue) 구현을 위해 deque 라이브러리 사용
   queue = deque([start])
   # 현재노드 방문처리
   visited[start] = True
   # 큐가 빌 때까지 반복
   while queue:
      # 큐에서 하나의 원소를 뽑아 출력
      v = queue.popleft()
      print(v, end= ' ')
      # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for i in graph[v]:
         if not visited[i]:
            queue.append(i)
            visited[i] = True


# bfs(graph, 1, visited)


# n - 세로, m - 가로
def py510():
   n, m = map(int, input().split())
   graph = []
   for i in range(n):
      graph.append(list(map(int, input().split())))

   def dfs2(x, y):
      if x <= -1 or x >= n or y <= -1 or y >= m:
         return False

      # 현재노드 방문하지 않았을 때
      if graph[x][y] == 0:

         # 해당 노드 방문처리
         graph[x][y] = 1

         # 상, 하, 좌, 우
         dfs2(x - 1, y)
         dfs2(x, y - 1)
         dfs2(x + 1, y)
         dfs2(x, y + 1)
         return True
      return False

   result = 0
   for i in range(n):
      for j in range(m):
         # 현재 위치에서 DFS 수행
         if dfs2(i, j) == True:
            result += 1

   # print(result)


# selection sort

def sel_sort():
   arr = [7,5,9,0,3,1,6,2,4,8]

   for i in range(len(arr)):
      min_idx = i
      for j in range(i + 1, len(arr)):
         if arr[min_idx] > arr[j]:
            min_idx = j
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
   return arr


def sel_sort2(xs):
   if xs != []:
      smallest = min(xs)
      xs.remove(smallest)
      return [smallest] + sel_sort2(xs)
   else:
      return []
   

# insertion sort

def insertion_sort():
   arr = [7,5,9,0,3,1,6,2,4,8]

   for i in range(1, len(arr)):
      for j in range(i, 0, -1):
         if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
         else:
            break
   return arr