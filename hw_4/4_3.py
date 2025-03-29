import multiprocessing
import time
import codecs
import threading

def timestamp():
    return time.strftime("[%H:%M:%S]")

# ======== Процесс A ========
def process_a(input_queue, a_to_b_queue):
    def forward_messages():
        while True:
            if not input_queue.empty():
                msg = input_queue.get()
                if msg == "__exit__":
                    break
                msg = msg.lower()
                print(f"{timestamp()} A получил сообщение: {msg}")
                time.sleep(5)  # ждем-с, так сказать
                a_to_b_queue.put(msg)
                print(f"{timestamp()} A отправил сообщение в B: {msg}")
            else:
                time.sleep(0.1)
    forward_messages()

# ======== Процесс B ========
def process_b(a_to_b_queue, b_to_main_queue):
    while True:
        if not a_to_b_queue.empty():
            msg = a_to_b_queue.get()
            if msg == "__exit__":
                break
            encoded = codecs.encode(msg, "rot_13")
            print(f"{timestamp()} B обработал и выводит: {encoded}")
            b_to_main_queue.put(encoded)
        else:
            time.sleep(0.1)

# ======== Главный процесс ========
def main():
    input_queue = multiprocessing.Queue()
    a_to_b_queue = multiprocessing.Queue()
    b_to_main_queue = multiprocessing.Queue()

    log_file = open("4_3_results.txt", "w", encoding="utf-8")

    def log(msg):
        print(msg)
        log_file.write(msg + "\n")
        log_file.flush()

    # Запуск процессов A и B
    proc_a = multiprocessing.Process(target=process_a, args=(input_queue, a_to_b_queue))
    proc_b = multiprocessing.Process(target=process_b, args=(a_to_b_queue, b_to_main_queue))
    proc_a.start()
    proc_b.start()

    # Фоновый поток для получения сообщений из процесса B
    def receive_from_b():
        while True:
            if not b_to_main_queue.empty():
                result = b_to_main_queue.get()
                if result == "__exit__":
                    break
                log(f"{timestamp()} Главный процесс получил от B: {result}")
            else:
                time.sleep(0.1)

    threading.Thread(target=receive_from_b, daemon=True).start()

    # Ввод пользователя
    log(f"{timestamp()} Введите сообщения:")
    try:
        while True:
            user_input = input()
            if user_input.strip().lower() == "exit":
                input_queue.put("__exit__")
                a_to_b_queue.put("__exit__")
                b_to_main_queue.put("__exit__")
                break
            log(f"{timestamp()} Пользователь ввел: {user_input}")
            input_queue.put(user_input)
    except KeyboardInterrupt:
        pass

    proc_a.join()
    proc_b.join()
    log_file.close()

if __name__ == "__main__":
    main()