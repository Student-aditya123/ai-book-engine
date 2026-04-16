import os
import sys
import django
import time

# Django setup
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from books.models import Book


def scrape_books():
    print("🚀 Scraper started...")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://books.toscrape.com/")
    time.sleep(2)

    print("📚 Collecting book links...")

    books = driver.find_elements(By.CLASS_NAME, "product_pod")
    book_links = []

    # Step 1: collect links first
    for book in books[:10]:
        link = book.find_element(By.TAG_NAME, "a").get_attribute("href")
        book_links.append(link)

    print(f"✅ Found {len(book_links)} books")

    # Step 2: visit each book
    for link in book_links:
        driver.get(link)
        time.sleep(1)

        title = driver.find_element(By.TAG_NAME, "h1").text

        try:
            description = driver.find_element(By.ID, "product_description") \
                .find_element(By.XPATH, "following-sibling::p").text
        except:
            description = "No description available"

        print("💾 Saving:", title)

        # Avoid duplicates
        if not Book.objects.filter(title=title).exists():
            Book.objects.create(
                title=title,
                description=description,
                url=link,
                rating="N/A"
            )

    driver.quit()
    print("✅ Scraping completed!")


# IMPORTANT: run function
if __name__ == "__main__":
    scrape_books()