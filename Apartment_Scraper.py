from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def element_exists(by, value, context):
    try:
        return context.find_element(by, value)
    except:
        return None

def get_total_pages(driver):
    try:
        page_range_text = driver.find_element(By.CSS_SELECTOR, '.pageRange').text
        total_pages = int(page_range_text.split()[-1])  # Extract the total number of pages
        return total_pages
    except Exception as e:
        print(f"Error getting total pages: {e}")
        return 1  # Default to 1 if unable to determine

def scrape_apartments(base_url):
    options = Options()
    options.headless = True  # Run headless Chrome

    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)

    wait = WebDriverWait(driver, 10)

    data = []

    def scrape_current_page():
        listings = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'placard')))

        for listing in listings:
            try:
                title_elem = element_exists(By.CLASS_NAME, 'property-title', listing)
                address_elem = element_exists(By.CLASS_NAME, 'property-address', listing)
                phone_elem = element_exists(By.CLASS_NAME, 'phone-link', listing)
                amenities_elem = element_exists(By.CLASS_NAME, 'property-amenities', listing)
                badge_elem = element_exists(By.CLASS_NAME, 'mortar-badge', listing)
                url_elem = element_exists(By.CLASS_NAME, 'property-link', listing)

                # Check for the presence of property-information-wrapper
                property_info_wrapper = element_exists(By.CLASS_NAME, 'property-information-wrapper', listing)
                if property_info_wrapper:
                    price_elem = element_exists(By.CLASS_NAME, 'price-range', property_info_wrapper)
                    beds_elem = element_exists(By.CLASS_NAME, 'bed-range', property_info_wrapper)
                else:
                    price_elem = element_exists(By.CLASS_NAME, 'property-pricing', listing)
                    beds_elem = element_exists(By.CLASS_NAME, 'property-beds', listing)

                title = title_elem.text if title_elem else None
                address = address_elem.text if address_elem else None
                price = price_elem.text if price_elem else None
                beds = beds_elem.text if beds_elem else None
                phone = phone_elem.text if phone_elem else None
                amenities = amenities_elem.text if amenities_elem else None
                badge = badge_elem.text if badge_elem else None
                url = url_elem.get_attribute('href') if url_elem else None

                data.append({
                    'Title': title,
                    'Address': address,
                    'Price': price,
                    'Beds': beds,
                    'Phone': phone,
                    'Amenities': amenities,
                    'Badge': badge,
                    'URL': url
                })
            except Exception as e:
                print(f"Error parsing listing: {e}")
                continue

    # Get the total number of pages
    total_pages = get_total_pages(driver)

    # Iterate through each page
    for page in range(1, total_pages + 1):
        if page > 1:
            page_url = f"{base_url}/{page}"
            driver.get(page_url)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'placard')))
        scrape_current_page()

    driver.quit()
    return data

base_url = "https://www.apartments.com/downtown-tampa-tampa-fl/min-2-bedrooms-under-3000"
data = scrape_apartments(base_url)

# Save data to a DataFrame and display
df = pd.DataFrame(data)
print(df)

# Save to a CSV file
df.to_csv('apartments_list.csv', index=False)
