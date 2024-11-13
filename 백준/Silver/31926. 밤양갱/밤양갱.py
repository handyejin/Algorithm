import sys
import math

n = int(sys.stdin.readline().strip())
print(8 + 1 + math.trunc(math.log2(n)) + 1)
