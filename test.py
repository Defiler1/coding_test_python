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



n = int(input())
direction_list = list(input().split())
direction_type = ['L', 'R', 'U', 'D']
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
x, y = 1, 1


for direction in direction_list:
   for i in range(len(direction_type)):
      if direction_type[i] == direction:
         ax = x + dx[i]
         ay = y + dx[i]
   if ax < 1 or ay < 1 or ax > n or ay > n:
      continue
   x, y = ax, ay

print(x, y)