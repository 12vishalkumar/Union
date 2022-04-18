# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
S1 = set(map(int, input().split()))
N2 = int(input())
S2 = set(map(int, input().split()))
print(len(S1.union(S2)))