YouTube Market Intelligence: Global Gastro-Tourism Trends 2026
📌 Project Overview
This project is a data engineering and analysis pipeline designed to compare the digital footprint of San Salvador’s culinary scene against major global tourism hubs: Tokyo, Bangkok, Paris, and Seoul. Using the YouTube Data API v3, I extracted and processed real-time metrics to identify engagement patterns and market opportunities for emerging travel destinations.

🛠️ Technical Stack
  Language: Python 3.x
    Data Extraction: YouTube Data API v3
      Data Processing: Pandas
        Environment Management: Python Virtual Environments (venv)
          Security: Dotenv (Environment Variables)
            Visualization: Power BI

🛡️ Security & Best Practices
To ensure industry-standard security, this project implements:
  Credential Masking: API keys are stored in a .env file and managed via python-dotenv.
    Version Control Safety: A .gitignore file is included to prevent sensitive credentials from being leaked to public repositories.
      Dependency Isolation: All libraries are managed within a local virtual environment for project reproducibility.

📊 Key Data Insights
  The final dataset consists of 50+ records with the following metrics: Views, Likes, Comments, and Publish Dates.
    San Salvador's Competitive Edge: One of the top-performing videos in the dataset belongs to San Salvador, with over 18.5 million views and 370k+ likes, demonstrating a high global interest in Salvadoran street food.
      Engagement Analysis: While cities like Paris and Tokyo lead in volume, San Salvador frequently shows higher Comment-to-View ratios, suggesting a more engaged and curious audience.

📖 Data Dictionary
  City: Target location for the search.
    Title: Video title (HTML unescaped for readability).
      Views/Likes/Comments: Real-time engagement metrics from YouTube API.
        Publish_Date: Original upload timestamp (ISO 8601 format).
          Video_URL: Direct link to the source video.

🚀 Setup & Installation
Clone the repository:
  git clone https://github.com/your-username/youtube-analysis.git
  cd youtube-analysis

Create and activate a virtual environment:
  python -m venv venv
  .\venv\Scripts\activate

Install dependencies:
  pip install -r requirements.txt

Configure API Key:
  Create a .env file in the root directory and add:
  YT_API_KEY=your_api_key_here