import os
import pandas as pd
import html
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables for security (API Key)
load_dotenv()
API_KEY = os.getenv("YT_API_KEY")

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Define target cities and search parameters
cities = ["San Salvador", "Tokyo", "Bangkok", "Paris", "Seoul"]
search_query = "best street food and places to visit"

def get_combined_data():
    """
    Fetches YouTube video search results and their respective statistics 
    for a list of defined cities, then exports the data to a CSV file.
    """
    all_data = []
    
    for city in cities:
        print(f"🚀 Processing data for: {city}...")
        
        # Step 1: Search for relevant videos per city
        request = youtube.search().list(
            q=f"{city} {search_query}",
            part="snippet",
            maxResults=10, 
            type="video",
            relevanceLanguage="en"
        )
        response = request.execute()

        # Handle cases where no videos are returned
        if not response.get('items'):
            print(f"⚠️ No videos found for {city}")
            continue

        for item in response['items']:
            video_id = item['id']['videoId']
            
            # Step 2: Request detailed statistics for each specific video ID
            stats_request = youtube.videos().list(
                part="statistics,snippet",
                id=video_id
            )
            stats_response = stats_request.execute()
            
            if stats_response.get('items'):
                video_data = stats_response['items'][0]
                stats = video_data['statistics']
                
                # Clean HTML entities from titles (e.g., &amp; to &)
                raw_title = item['snippet']['title']
                clean_title = html.unescape(raw_title)
                
                # Store cleaned data into the list
                all_data.append({
                    'City': city,
                    'Title': clean_title,
                    'Views': int(stats.get('viewCount', 0)),
                    'Likes': int(stats.get('likeCount', 0)),
                    'Comments': int(stats.get('commentCount', 0)),
                    'Publish_Date': item['snippet']['publishedAt'],
                    'Video_URL': f"https://www.youtube.com/watch?v={video_id}"
                })

    # Step 3: Export collected data to a CSV file
    if all_data:
        df = pd.DataFrame(all_data)
        
        # Sort data by View Count to highlight top performers
        df = df.sort_values(by='Views', ascending=False)
        
        # Define output path and export using UTF-8-SIG for Excel compatibility
        path = os.path.join(os.getcwd(), 'gastro_tourism_final.csv')
        df.to_csv(path, index=False, encoding='utf-8-sig')
        print(f"\n✅ DATASET CREATED: {path}")
    else:
        print("\n❌ ERROR: No data was collected. Please check your API Key and Quota.")

if __name__ == "__main__":
    get_combined_data()