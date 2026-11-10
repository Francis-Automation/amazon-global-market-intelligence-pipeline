import os
import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def initialize_driver():
    options = webdriver.FirefoxOptions()
    options.width = 1920
    options.height = 1080
    options.set_preference("log.level", "fatal")
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0")
    options.set_preference("intl.accept_languages", "en-GB,en;q=0.9")
    options.set_preference("geo.enabled", False)
    options.set_preference("permissions.default.image", 2)
    options.page_load_strategy = "eager"
    return webdriver.Firefox(options=options)

def create_database():
    filename = "market_prices.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Product Name", "Price", "Source URL", "Status"])

def extract_product_data(driver, target_url, page_num):
    print(f"[*] Page {page_num}/10")
    try:
        driver.set_page_load_timeout(25)
        driver.get(target_url)
        try:
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "sp-cc-accept"))).click()
        except:
            pass
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.5);")
        time.sleep(1.5)
        cards = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for card in cards[:5]:
            try:
                title = card.find_element(By.CSS_SELECTOR, "h2 span").text.strip()
            except:
                title = "Unknown Product"
            price = "N/A"
            try:
                price = card.find_element(By.CSS_SELECTOR, "span.a-price span.a-offscreen").get_attribute("textContent").strip()
            except:
                if "£" in card.text:
                    for l in card.text.split("\n"):
                        if "£" in l:
                            price = l.strip()
                            break
            if "£" not in str(price) and price != "N/A":
                price = f"£{price}"
            print(f" -> {title[:40]} | {price}")
            with open("market_prices.csv", mode='a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow([timestamp, title, price, target_url, "SUCCESS"])
    except:
        print(f"[-] Skip page {page_num}")

if __name__ == "__main__":
    create_database()
    browser = initialize_driver()

    # GLOBAL MARKET TOGGLE - Switch niche here
    search_keyword = "supplements"       # Health & Wellness
    # search_keyword = "clothing"          # Fashion & Apparel
    # search_keyword = "skincare cream"    # Beauty & Personal Care
    # search_keyword = "school bag"        # School & Education Market

    try:
        for page in range(1, 11):
            url = f"https://www.amazon.co.uk/s?k={search_keyword}&language=en_GB&currency=GBP&page={page}"
            extract_product_data(browser, url, page)
            time.sleep(4)
    finally:
        browser.quit()
        print("[✓] Completed")
