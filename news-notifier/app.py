import requests
from plyer import notification
import time
import random

TOPICS = [
    'technology', 'coding', 'programming', 'software', 'hardware', 'artificial intelligence', 
    'machine learning', 'data science', 'cybersecurity', 'cloud computing', 'internet of things',
    'web development', 'mobile development', 'devops', 'software engineering', 'blockchain', 
    'cryptocurrency', 'virtual reality', 'augmented reality', 'robotics', 'quantum computing',
    'big data', 'networking', 'database management', 'IT infrastructure', 'computer science', 
    'game development', 'UI/UX design', 'frontend development', 'backend development', 'e-commerce',
    'digital marketing', 'tech startups', 'IT careers', 'tech trends', 'tech innovations'
]

while True:
    # Select a random topic
    topic = random.choice(TOPICS)
    
   
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey=7cbb049d9dcb421e84db5e0a3175f487'
    response = requests.get(url)
    news_data = response.json()
    
    
    articles = news_data.get('articles', [])
    
    if articles:
        # Select a random article
        article = random.choice(articles)
        
       
        title = article.get('title', 'No Title')
        description = article.get('description', 'No Description')
        source = article.get('source', {}).get('name', 'No Source')
        published_date = article.get('publishedAt', 'No Date')
        
       
        title = title[:30]
        description = description.split(".")[0]
        
        
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Source: {source}")
        print(f"Published Date: {published_date}")
        print("\n---\n")
      
        notification.notify(
            title=f"{title} - {source}",
            app_icon='icon.ico',
            message=f"{description}\nPublished on: {published_date}",
            timeout=10  # Notification timeout in seconds
        )
    time.sleep(2 * 60 * 60)
