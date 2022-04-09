n = int(input())
milk = []
for i in range(n):
    milk.append(int(input()))
milk.sort(reverse = True)

total_milk= 0
a = n // 3
b = n % 3
for i in range(a):
    total_milk += milk[3 * i] + milk[3 * i + 1]
if b == 2:
    total_milk += milk[n - 1] + milk[n - 2]
elif b == 1:
    total_milk += milk[n - 1]

print(total_milk)
