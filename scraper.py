from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pymongo
import uuid
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# MongoDB connection
def connect_to_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client['twitter_trends']

def fetch_trending_topics():
    # Configure EdgeDriver options
    options = Options()
    options.add_argument("--start-maximized")

    # Set up EdgeDriver (Make sure the path is correct for msedgedriver.exe)
    driver = webdriver.Edge(service=Service(r'C:\Users\karth\Downloads\edgedriver_win64\msedgedriver.exe'), options=options)

    try:
        # Open Twitter login page
        driver.get("https://twitter.com/login")
        time.sleep(5)

        # Add login logic (username and password)
        username_field = driver.find_element(By.NAME, "text")
        username_field.send_keys("MitmartB74475")  # Replace with your username
        username_field.send_keys(Keys.RETURN)
        time.sleep(2)

        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("Indrajit@9")  # Replace with your password
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

        # Wait for the trends section to be visible
        try:
            print("Waiting for trends to load...")
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-testid='trend']"))
            )
            print("Trends section found.")
            
            # Get the trending topics
            topics = driver.find_elements(By.XPATH, "//div[@data-testid='trend']//span[contains(text(), '#')]")
            if topics:
                print(f"Found {len(topics)} topics.")
                topics_list = [topic.text for topic in topics[:5]]  # Get the top 5 topics
            else:
                print("No topics found.")
                topics_list = []

        except Exception as e:
            print(f"Error while scraping topics: {e}")
            topics_list = []

        # Prepare data for MongoDB
        unique_id = str(uuid.uuid4())
        timestamp = datetime.datetime.now()
        ip_address = "127.0.0.1"

        data = {
            "_id": unique_id,
            "topics": topics_list,
            "timestamp": timestamp,
            "ip_address": ip_address
        }

        # Store data in MongoDB
        db = connect_to_mongo()
        db['topics'].insert_one(data)

        return data

    finally:
        driver.quit()
