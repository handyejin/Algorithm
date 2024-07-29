import math
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(math.comb(m, n))
