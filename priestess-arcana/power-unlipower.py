def solve(e,t):
    return pow(e,t,10**7)
  

e, t = list(map(int,input().rstrip().split(" ")))
print(solve(e,t))