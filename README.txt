Twitter Trends Scraper

This project is a Python-based web scraping application that automates the extraction of the top 5 trending topics from Twitter's "What's Happening" section. The scraped data is stored in MongoDB and displayed on a simple Flask web application.

Features

Web Scraping: Utilizes Selenium to log in to Twitter and scrape trending topics.

Dynamic IP Handling: (Optional) Can integrate with proxy services for IP rotation.

Database Storage: Stores data in a MongoDB database, including metadata like execution time and IP address.

Web Interface: A Flask web application provides a user-friendly interface to trigger the scraper and display results.

Requirements

Software

Python 3.8 or higher

MongoDB (running locally)

Microsoft Edge browser

EdgeDriver (matching your Edge version)

Python Libraries

Install the required Python packages using:

pip install -r requirements.txt

requirements.txt:

selenium
pymongo
Flask

Project Structure

project/
├── selenium_script/
│   ├── scraper.py            # Contains the Selenium script for scraping Twitter
│   ├── msedgedriver.exe      # EdgeDriver executable
│   
├── database/
│   ├── connect_mongodb.py    # MongoDB connection setup
│   
├── web/
│   ├── app.py               # Flask web application
│   ├── templates/
│       ├── index.html       # HTML interface for the web app

README.md                     # Project documentation
requirements.txt              # Python dependencies

Setup Instructions

1. Install Dependencies

Install Python Libraries:

pip install -r requirements.txt

Install MongoDB:

Download and install MongoDB Community Server from mongodb.com.

Start MongoDB:

mongod --dbpath="C:\data\db"

Download EdgeDriver:

Visit EdgeDriver Downloads.

Download the version matching your Edge browser.

Place the msedgedriver.exe file in the selenium_script/ directory.

2. Configure the Project

Twitter Credentials:

Replace the placeholders in scraper.py with your Twitter username and password:

username_field.send_keys("your_twitter_username")
password_field.send_keys("your_twitter_password")

Set Up MongoDB:

Ensure MongoDB is running locally on localhost:27017.

Verify EdgeDriver Path:

Ensure the msedgedriver.exe path is correct in scraper.py:

driver = webdriver.Edge(service=Service('./selenium_script/msedgedriver.exe'), options=options)

Usage

1. Start the MongoDB Server

Run the following command:

mongod --dbpath="C:\data\db"

2. Run the Flask Application

Navigate to the web/ directory and start the Flask server:

python app.py

3. Access the Web Interface

Open a browser and go to:

http://127.0.0.1:5000

Click the "Run Script" button to execute the scraper.

4. Verify Data in MongoDB

Open the MongoDB shell:

mongo

View the stored records:

use twitter_trends
db.trends.find().pretty()

Expected Output

Web Interface

When the script is run, the web page will display:

The top 5 trending topics on Twitter.

The timestamp of when the script was executed.

The IP address used for the request.

MongoDB Record

A sample record stored in MongoDB:

{
  "_id": "unique_id",
  "trends": [
    "#Trend1",
    "#Trend2",
    "#Trend3",
    "#Trend4",
    "#Trend5"
  ],
  "timestamp": "2024-12-27T10:00:00",
  "ip_address": "127.0.0.1"
}

Troubleshooting

Common Issues

NoSuchDriverException:

Ensure msedgedriver.exe is correctly placed and the path is accurate.

MongoDB Connection Error:

Verify MongoDB is running on localhost:27017.

Twitter Login Issues:

Test your Twitter credentials manually to ensure there are no CAPTCHA challenges.

Blank Page in Browser:

Confirm index.html is in the templates/ directory.