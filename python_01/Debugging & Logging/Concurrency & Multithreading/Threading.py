import threading

def task():
    print("Task running")

t = threading.Thread(target=task)
t.start()
t.join()
