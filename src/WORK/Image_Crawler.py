from CONSTANT import DATA_FOLDER_PATH
from UTILITY import logln_info
import os


from icrawler.builtin import GoogleImageCrawler  # type: ignore


def download_images(query, num_images, output_dir):
    google_crawler = GoogleImageCrawler(storage={"root_dir": output_dir})
    google_crawler.crawl(keyword=query, max_num=num_images)

# Beispiel: 200 Bilder der Pflanze "Erdbeere" herunterladen

if __name__ == "__main__":
    logln_info(f"Erdbeere: {os.path.join(DATA_FOLDER_PATH, "dataset", "erdbeere")}")
    download_images("Erdbeere", 200, os.path.join(DATA_FOLDER_PATH, "dataset", "erdbeere"))
# 
