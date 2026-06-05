# finalle
Mkopo
# MIXX BY YAS - Loan Application Website

A simple loan application website built with:

- HTML
- CSS
- JavaScript
- Python Flask
- Telegram Bot API

## Project Structure

project/

├── index.html

├── style.css

├── script.js

├── app.py

├── requirements.txt

└── README.md

## Features

- Loan application form
- Responsive design
- Flask backend
- Sends applications to Telegram
- Ready for Render deployment

## Environment Variables

Create the following variables in Render:

BOT_TOKEN=YOUR_BOT_TOKEN

CHAT_ID=YOUR_CHAT_ID

## Render Settings

Build Command:

pip install -r requirements.txt

Start Command:

gunicorn app:app

## Local Run

Install dependencies:

pip install -r requirements.txt

Run:

python app.py

Open:

http://localhost:5000

## Telegram Setup

1. Create a bot using @BotFather
2. Copy the bot token
3. Get your Telegram chat ID
4. Add BOT_TOKEN and CHAT_ID to Render
5. Deploy

## Author

MIXX BY YAS
