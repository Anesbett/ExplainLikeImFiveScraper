import json

class QueryEngine:
    def __init__(self, config_file='settings.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get_reddit_posts(self, query, subreddit='ExplainLikeImFive', limit=5):
        import praw
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
