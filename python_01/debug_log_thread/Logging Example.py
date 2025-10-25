import logging
import time
import random

# Configure the logger
logging.basicConfig(
    filename='download_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def download_file(file_name):
    logging.info(f"Started downloading {file_name}")
    try:
        # Simulate random download times and errors
        time.sleep(random.uniform(1, 3))
        if random.choice([True, False]):
            raise ConnectionError("Network interrupted")

        logging.info(f"Successfully downloaded {file_name}")

    except Exception as e:
        logging.error(f"Failed to download {file_name}: {e}")

def main():
    files = ["video.mp4", "image.png", "notes.pdf", "music.mp3"]
    logging.info("Download process started")

    for f in files:
        download_file(f)

    logging.info("All downloads completed")

if __name__ == "__main__":
    main()
