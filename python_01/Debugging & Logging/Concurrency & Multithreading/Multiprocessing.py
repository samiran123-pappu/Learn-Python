from multiprocessing import Process

def task():
    print("Running in separate process")

p = Process(target=task)
p.start()
p.join()
