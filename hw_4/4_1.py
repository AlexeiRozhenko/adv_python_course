import time
import threading
import multiprocessing

# Числа Фибоначчи
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Логирование с временной меткой
def log(message):
    timestamp = time.strftime("%H:%M:%S")
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


# Вспомогательная функция
def worker(n, results, index):
    log(f"Запуск fib({n}) в потоке/процессе {index}")
    start = time.perf_counter()
    results[index] = fib(n)
    end = time.perf_counter()
    log(f"Завершение fib({n}) в потоке/процессе {index} за {end - start:.4f} секунд")


# Синхронный запуск
def run_sync(n, count=10):
    results = []
    log("=== СИНХРОННЫЙ ЗАПУСК ===")
    start = time.perf_counter()
    for i in range(count):
        log(f"Синхронно запускаем fib({n}), итерация {i}")
        t0 = time.perf_counter()
        results.append(fib(n))
        t1 = time.perf_counter()
        log(f"Завершено: итерация {i} за {t1 - t0:.4f} секунд")
    total_time = time.perf_counter() - start
    log(f"Общее время (синхронно): {total_time:.4f} секунд\n")
    return total_time, results


# Потоки
def run_threading(n, count=10):
    log("=== ПОТОКИ ===")
    threads = []
    results = [None] * count
    start = time.perf_counter()
    for i in range(count):
        t = threading.Thread(target=worker, args=(n, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    total_time = time.perf_counter() - start
    log(f"Общее время (потоки): {total_time:.4f} секунд\n")
    return total_time, results


# Процессы
def run_multiprocessing(n, count=10):
    log("=== ПРОЦЕССЫ ===")
    manager = multiprocessing.Manager()
    results = manager.list([None] * count)
    processes = []
    start = time.perf_counter()
    for i in range(count):
        p = multiprocessing.Process(target=worker, args=(n, results, i))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    total_time = time.perf_counter() - start
    log(f"Общее время (процессы): {total_time:.4f} секунд\n")
    return total_time, list(results)


def main():
    n = 35
    count = 10

    # Очищаем файл перед началом
    with open("4_1_results.txt", "w", encoding="utf-8") as f:
        f.write("=== ЗАПУСК ===\n")

    # Синхронное выполнение
    sync_time, _ = run_sync(n, count)
    
    # Потоки
    threading_time, _ = run_threading(n, count)
    
    # Процессы
    multiprocessing_time, _ = run_multiprocessing(n, count)

    # Финальное резюме
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write("=== ИТОГИ ===\n")
        f.write(f"Синхронное выполнение: {sync_time:.4f} секунд\n")
        f.write(f"Параллельное выполнение (потоки): {threading_time:.4f} секунд\n")
        f.write(f"Параллельное выполнение (процессы): {multiprocessing_time:.4f} секунд\n")


if __name__ == "__main__":
    main()