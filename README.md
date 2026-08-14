Thirukkural App

A simple mobile-friendly Flask web application for exploring Thirukkural using the Thirukkural API.

Features

Search Kural by number

Random Kural

Save favourite Kurals

Saved Kurals

Light and Dark Mode

Listen using Text-to-Speech

Share Kural

Responsive mobile UI

No SQL database

Tech Stack

Python

Flask

HTML

CSS

JavaScript

REST API

How It Works

User
 ↓
Web UI
 ↓
Flask Backend
 ↓
Thirukkural API
 ↓
JSON Response
 ↓
Kural Display

Project Structure

thirukkural_app/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── services/
│   └── thirukkural_api.py
├── templates/
│   └── index.html
└── screenshots/
    ├── home-light.png
    ├── homedark.png
    └── saved.png

Screenshots

Home - Light Mode
screenshots/home-light.png



Saved Kurals
screenshots/saved.png




Home - Dark Mode
screenshots/saved.png



Run Locally

pip install -r requirements.txt
python app.py

Open:

http://127.0.0.1:5000

API

Thirukkural API:

https://thirukkural.docs.apiary.io/

Author

Keerthana.K
