# Zuerst installieren:
# pip install icrawler

from icrawler.builtin import GoogleImageCrawler  # type: ignore

def download_images(query, num_images, output_dir):
    google_crawler = GoogleImageCrawler(storage={'root_dir': output_dir})
    google_crawler.crawl(keyword=query, max_num=num_images)

# Beispiel: 200 Bilder der Pflanze "Erdbeere" herunterladen
download_images('Erdbeere', 200, 'dataset/erdbeere')

# Wiederhole das für weitere Pflanzenarten, z.B.:
download_images('Tomate', 200, 'dataset/tomate')
download_images('Basilikum', 200, 'dataset/basilikum')
