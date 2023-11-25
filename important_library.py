import time


N_ITER: 'int' = 1_000_000


def cpu_task() -> 'int':
    res: 'int' = 0
    for i in range(N_ITER):
        if not i % 2023:
            res += i    
    return res


def io_task() -> 'None':
    for i in range(N_ITER):
        time.sleep(0.00000001)
