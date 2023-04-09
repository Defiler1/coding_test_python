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