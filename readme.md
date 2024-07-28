# Reddit Query App

Welcome to the Reddit Query App! This application allows you to search for posts in the `r/ExplainLikeImFive` subreddit using the Reddit API. The application is built using the `wxPython` library for the graphical user interface and `praw` for interacting with the Reddit API.

## Features

- Search for posts in the `r/ExplainLikeImFive` subreddit.
- Display the results including the title, score, and URL of the posts.
- Simple and intuitive graphical user interface.

## Requirements

- Python 3.x
- wxPython
- praw
- python-dotenv

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Anesbett/ExplainLikeImFiveScraper.git
   cd ExplainLikeImFiveScraper
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your Reddit API credentials:

   ```
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   USER_AGENT=your_user_agent
   ```
   or use the "settings" button when starting the applicaiton 

## Usage

1. Run the application:

   ```sh
   python main.py
   ```

2. Enter a query in the text input field and click the "Search" button to fetch posts from Reddit.

## Code Overview

### `main.py`

This file sets up the main application window using `wxPython` and handles user interactions such as entering a query and displaying search results.

### `Menu.py`

This file sets up the menu bar for the application.

### `QueryEngine.py`

This file contains the `QueryEngine` class, which handles loading configuration from the `.env` file and fetching posts from Reddit using `praw`.

### Environment Variables

The application uses the following environment variables, which should be set in a `.env` file:

- `CLIENT_ID`: Your Reddit API client ID.
- `CLIENT_SECRET`: Your Reddit API client secret.
- `USER_AGENT`: A user agent string for your Reddit application.

# My idea
Here is my idea that I had as I just wanted to practice python and create something. 

![alt text](image.png)