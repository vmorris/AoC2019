import time


def run_timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        run_time = end_time - start_time
        print(f'runtime: {run_time:.3f} seconds')
    return wrapper
