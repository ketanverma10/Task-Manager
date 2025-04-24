import requests
from utils.styling import success_message

def get_quote():
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)
        
        if response.status_code == 200:
            quote_data = response.json()
            quote = quote_data[0]['q']  # Extract quote text
            author = quote_data[0]['a']  # Extract author name
            
            success_message(f"Motivational Quote: '{quote}' - {author}")
        else:
            success_message("Stay strong. Stay motivated. 💪")
    
    except Exception as e:
        success_message(f"Push yourself, because no one else is going to do it for you. 🚀")
