import os
from dotenv import load_dotenv
import praw

class QueryEngine:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()
        self.load_config()  # Load the configuration from .env

    def get_reddit_posts(self, query, subreddit='ExplainLikeImFive', limit=5):
        """Fetch posts from Reddit based on a search query."""
        reddit = praw.Reddit(
            client_id=self.config['client_id'],
            client_secret=self.config['client_secret'],
            user_agent=self.config['user_agent']
        )
        
        results = reddit.subreddit(subreddit).search(query, limit=limit)
        posts = []
        for submission in results:
            posts.append({
                'title': submission.title,
                'score': submission.score,
                'url': submission.url
            })
        
        return posts

    def print_config(self):
        """Print the current configuration values."""
        print(f"Client ID: {self.config['client_id']}")
        print(f"Client Secret: {self.config['client_secret']}")
        print(f"User Agent: {self.config['user_agent']}")
    
    def save_config(self):
        """Save the current configuration to a .env file."""
        with open('.env', 'w') as f:
            for key, value in self.config.items():
                f.write(f"REDDIT_{key.upper()}={value}\n")

    def load_config(self):
        """Load configuration from the .env file."""
        self.config = {
            'client_id': os.getenv('CLIENT_ID', ''),
            'client_secret': os.getenv('CLIENT_SECRET', ''),
            'user_agent': os.getenv('USER_AGENT', 'myRedditApp/0.1 by myUsername (a tool for querying Reddit)')
        }
