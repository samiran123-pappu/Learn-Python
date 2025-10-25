import threading
import time
import logging

# Configure logging for threads
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s: %(message)s'
)

def worker(task_name, duration):
    logging.info(f"Starting {task_name}")
    time.sleep(duration)
    logging.info(f"Completed {task_name}")

def main():
    tasks = [
        ("Download Images", 2),
        ("Process Data", 4),
        ("Upload Report", 3),
        ("Send Notifications", 1)
    ]

    threads = []

    # Create and start threads
    for name, duration in tasks:
        t = threading.Thread(target=worker, args=(name, duration))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    logging.info("✅ All tasks completed!")

if __name__ == "__main__":
    main()
