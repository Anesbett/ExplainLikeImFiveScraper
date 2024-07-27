import praw

def get_reddit_posts(query, subreddit='ExplainLikeImFive', limit=5):
    """Fetch posts from Reddit based on a search query."""
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
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
