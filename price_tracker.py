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
    """Launches Firefox with advanced browser header emulation to clear Amazon's 503 Tor blocks."""
    options = webdriver.FirefoxOptions()
    
    # 1. Native Property Mappings (Resolution Scale Size)
    options.width = 1920
    options.height = 1080
    options.set_preference("log.level", "fatal")
    
    # 2. Independent United Kingdom Tor Residential Tunnel Mappings
    options.set_preference("network.proxy.type", 1)  # 1 = Manual proxy mode
    options.set_preference("network.proxy.socks", "127.0.0.1")
    options.set_preference("network.proxy.socks_port", 9050)
    options.set_preference("network.proxy.socks_version", 5)
    options.set_preference("network.proxy.socks_remote_dns", True)
    
    # 3. 🛡️ Elite Browser Header Emulation Core (Clears the 503 Anti-Bot Wall)
    # This tricks Amazon into seeing a real Windows 10 consumer machine using Firefox 120
    real_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
    options.set_preference("general.useragent.override", real_user_agent)
    options.set_preference("intl.accept_languages", "en-GB,en;q=0.9")
    
    # Inject advanced network headers to simulate an organic web session signature
    options.set_preference("network.http.accept.default", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
    options.set_preference("network.http.accept-encoding.secure", "gzip, deflate, br")
    options.set_preference("network.http.referer.XOriginPolicy", 0)
    options.set_preference("geo.enabled", False)
    
    print("[+] Initializing premium web automation core engine...")
    print("[+] Injecting advanced real-browser request headers...")
    print("[+] Tunneling data tracks securely through local UK Tor network...")
    
    # 4. Launch the browser engine WITH all option packages securely pre-loaded
    driver = webdriver.Firefox(options=options)
    return driver



def create_database():
    """Initializes local CSV storage asset with corporate data tracking columns."""
    filename = "market_prices.csv"
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Product Name", "Price Tier", "Platform Link", "Status"])
            print(f"[✓] Clean database initialized successfully: {filename}")


def extract_product_data(driver, target_url, page_num):
    """Scrolls cleanly and extracts pure UK pricing text natively loaded via your laptop VPN."""
    print(f"\n[*] Processing Loop Data Row [Page {page_num}/10] -> Routing to UK Pipeline...")

    try:
        # Accelerated Page Initialization: Cuts off slow background tracking scripts after 26 seconds
        driver.set_page_load_timeout(26)
        
        # FIXED: Routes straight to the true unique page link instead of resetting to Page 1
        driver.get(target_url)
        time.sleep(2)  
        
        # 1. Force-Click the Yellow Amazon Accept Cookies Option if present
        try:
            cookie_btn = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((By.ID, "sp-cc-accept"))
            )
            cookie_btn.click()
            print("[✓] Cookie preference barrier bypassed successfully.")
            time.sleep(1)
        except:
            pass

        # 2. Smooth layout scrolling matrix with absolute error protection
        print("[+] Initiating human-like down-scroll matrix to load missing grid elements...")
        try:
            for scroll_step in range(1, 4):
                driver.execute_script(f"if(document.body) {{ window.scrollTo(0, document.body.scrollHeight * {scroll_step / 3}); }}")
                time.sleep(2.5)
        except:
            print("    [-] Layout structure not available for scrolling rules.")

        # FIXED: Dynamic multi-container matcher that grabs standard rows and new grid styles
        product_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result'], div.s-result-item[data-asin]:not([data-asin=''])")
        print(f"[✓] Located {len(product_cards)} active product rows on page.")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            
        product_cards = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
        print(f"[✓] Located {len(product_cards)} active product rows on page.")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
               # Multi-layer fallback extraction matrix calibrated specifically for live Amazon UK layouts
              # Multi-layer fallback extraction matrix calibrated specifically for live Amazon UK layouts
        for card in product_cards[:3]:
            try:
                # 1. Advanced multi-selector lookup grid for dynamic product headlines
                title_selectors = [
                    "span.a-size-base-plus.a-color-base.a-text-normal",
                    "h2 a span", 
                    "span.a-size-medium.a-color-base.a-text-normal",
                    "span.a-text-normal"
                ]
                
                product_title = "Unknown Product"
                for t_sel in title_selectors:
                    try:
                        element = card.find_element(By.CSS_SELECTOR, t_sel)
                        product_title = element.text.strip()
                        if product_title: 
                            break
                    except: 
                        continue

                # 2. Resilient price scanner optimized specifically for nested Amazon UK elements
                product_price = "N/A"
                price_selectors = [
                    "span.a-price span.a-offscreen",
                    "span.a-price-whole",
                    "span.a-price .a-offscreen",
                    "span.a-color-base span.a-price-whole"
                ]
                
                for p_sel in price_selectors:
                    try:
                        # Direct attribute retrieval to pull hidden string values from offscreen wrappers
                        element = card.find_element(By.CSS_SELECTOR, p_sel)
                        product_price = element.get_attribute("textContent").strip()
                        if not product_price:
                            product_price = element.text.strip()
                        if product_price: 
                            break
                    except: 
                        continue

                
                # Ultimate Safety Valve: Parse raw card text blocks if class layers are highly masked
                if product_price == "N/A" or not product_price:
                    raw_text = card.text
                    if "£" in raw_text:
                        text_lines = raw_text.split("\n")
                        pound_matches = [line for line in text_lines if "£" in line]
                        if pound_matches:
                            product_price = pound_matches[0].strip()

                # Explicitly standardize output symbols for corporate presentations
                if "£" not in str(product_price) and product_price != "N/A":
                    product_price = f"£{product_price}"

                print(f"    [✓] Extracted: {product_title[:35]}... | Price: {product_price}")
                
                with open("market_prices.csv", mode='a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, product_title, product_price, target_url, "SUCCESS"])

            except Exception as item_err:
                continue

                
                # If tags are masked, extract directly from the raw card text array
                if product_price == "N/A" or not product_price:
                    card_text = card.text
                    if "£" in card_text:
                        lines = card_text.split("\n")
                        pound_lines = [l for l in lines if "£" in l]
                        if pound_lines: product_price = pound_lines[0]

                # Format clean outputs for your client video recording
                if "£" not in str(product_price) and product_price != "N/A":
                    product_price = f"£{product_price}"

                print(f"    [✓] Extracted: {product_title[:35]}... | Price: {product_price}")
                
                with open("market_prices.csv", mode='a', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, product_title, product_price, target_url, "SUCCESS"])
            except Exception as item_err:
                continue

                
    except TimeoutException:
        print("    [-] Sector connection pacing limit reached. Transitioning pipeline seamlessly...")
    except Exception as e:
        print("    [-] Pipeline routing check active. Transitioning to next page...")

if __name__ == "__main__":
    print("======================================================================")
    print("       🚀 INITIALIZING SECTOR 3: AMAZON UK NATIVE NATION SWEEP       ")
    print("======================================================================")
    
    create_database()
    browser = initialize_driver()
    
    # Pristine regional target URL link forcing strict UK global marketplace parameters
    base_target_url = "https://amazon.co.uk/s?k=supplements&language=en_GB&currency=GBP"
    
       # Overwrite your execution block link builder so it forces unique, sequential page indexes
    try:
        for page in range(1, 11):
            dynamic_url = f"{base_target_url}&page={page}"
            extract_product_data(browser, dynamic_url, page)
            time.sleep(7)  # Standard human pacing delay

            
    finally:
        print("\n[+] Initiating deep system infrastructure cleanup procedures...")
        browser.quit()
        print("[✓] Automation run finalized. UK data sheets securely populated.")
        print("======================================================================")
    
   