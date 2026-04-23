# YouTube Market Intelligence: Global Gastro-Tourism Trends 2026

## 📌 Project Overview
This project is a **data engineering and analysis pipeline** designed to compare the digital footprint of San Salvador’s culinary scene against major global tourism hubs: Tokyo, Bangkok, Paris, and Seoul. Using the **YouTube Data API v3**, I extracted and processed real-time metrics to identify engagement patterns and market opportunities.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Data Extraction:** YouTube Data API v3
* **Data Processing:** Pandas
* **Environment Management:** Python Virtual Environments (venv)
* **Security:** Dotenv (Environment Variables)
* **Visualization:** Tableau / Power BI

## 🛡️ Security & Best Practices
To ensure industry-standard security, this project implements:
* **Credential Masking:** API keys are stored in a `.env` file and managed via `python-dotenv`.
* **Version Control Safety:** A `.gitignore` file is included to prevent sensitive credentials from being leaked.
* **Dependency Isolation:** All libraries are managed within a local virtual environment for project reproducibility.

## 📊 Key Data Insights
* **Dataset:** 50+ records with metrics: Views, Likes, Comments, and Publish Dates.
* **San Salvador's Competitive Edge:** Identified top-performing content with over **18.5 million views**, demonstrating high global interest.
* **Engagement Analysis:** San Salvador frequently shows higher **Comment-to-View ratios**, suggesting a more engaged audience.

## 🚀 Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/paobonilla/youtube-analysis.git](https://github.com/paobonilla/youtube-analysis.git)
   cd youtube-analysis

Create and activate a virtual environment:
 python -m venv venv
.\venv\Scripts\activate

Install dependencies:
  pip install -r requirements.txt

Configure API Key:
  Create a .env file in the root directory and add:
  YT_API_KEY=your_api_key_here
