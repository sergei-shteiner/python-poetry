import time

N = 142857

for i in range(1, 8):
    print(f">>> {N} * {i}")
    time.sleep(3)
    print(N * i)
    time.sleep(4)