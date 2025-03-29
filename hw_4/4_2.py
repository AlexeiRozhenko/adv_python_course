import math
import time
import concurrent.futures
import multiprocessing


# Основная функция-воркер (анализирует определенный отрезок)
def integrate_range(f, a, b, n_iter):
    acc = 0.0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


# Параллелельное выполнение с выбором executor
def parallel_integrate(f, a, b, *, n_jobs=1, n_iter=10_000_000, executor_type='thread'):
    step = (b - a) / n_jobs
    iters_per_job = n_iter // n_jobs

    ranges = [(a + i * step, a + (i + 1) * step, iters_per_job) for i in range(n_jobs)]

    if executor_type == 'thread':
        Executor = concurrent.futures.ThreadPoolExecutor
    elif executor_type == 'process':
        Executor = concurrent.futures.ProcessPoolExecutor
    else:
        raise ValueError("executor_type must be 'thread' or 'process'")

    with Executor(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_range, f, start, end, iters) for (start, end, iters) in ranges]
        results = [future.result() for future in futures]

    return sum(results)


def main():
    a = 0
    b = math.pi / 2
    n_iter = 10_000_000
    max_jobs = multiprocessing.cpu_count() * 2

    results = []

    for n_jobs in range(1, max_jobs + 1):
        # Thread
        start = time.perf_counter()
        result_thread = parallel_integrate(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type='thread')
        duration_thread = time.perf_counter() - start

        # Process
        start = time.perf_counter()
        result_process = parallel_integrate(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type='process')
        duration_process = time.perf_counter() - start

        results.append((n_jobs, duration_thread, duration_process))

        print(f"n_jobs={n_jobs} | Thread: {duration_thread:.4f}s | Process: {duration_process:.4f}s")

    # Запись результатов
    with open("4_2_results.txt", "w", encoding="utf-8") as f:
        f.write("n_jobs\tThread_time\tProcess_time\n")
        for n_jobs, thread_time, process_time in results:
            f.write(f"{n_jobs}\t{thread_time:.6f}\t{process_time:.6f}\n")


if __name__ == "__main__":
    main()