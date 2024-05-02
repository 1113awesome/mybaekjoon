n= int(input()) 
n_list = input()
v = int(input())

if len(n_list.split()) == n :
    number_list = list(map(int, n_list.split()))

print(number_list.count(v))