from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def filter_bmp_characters(text):
    """Remove unsupported emoji or special unicode characters."""
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

name = ["your contact"]
message = "kha was ye delete ka za."

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Scan QR code and press ENTER...")

while True:
    print(f"Sending message to {name[0]}...")

    # Find and click the search box
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    search_box.clear()
    search_box.send_keys(name[0])
    search_box.send_keys(Keys.ENTER)



    # Find message box and send message
    message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
    message_box.send_keys(filter_bmp_characters(message))
    message_box.send_keys(Keys.ENTER)

    print(f"Message sent to {name[0]}")

print("✅ All messages sent successfully!")
driver.quit()
