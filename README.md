# Social Media Manager for NASA's Twitter

## Overview
This *Social Media Manager* is a conversational Streamlit application designed to analyze and derive insights from NASA's Twitter engagement data. Powered by LangChain, OpenAI's GPT-4, and a SQL database, it enables users to interactively query and explore tweets, calculate engagement metrics, and generate comparative insights across different post types (text, image, video, gif).

## Features
- *Chat-Based Interaction*: A user-friendly interface to query the database using natural language.
- *SQL Database Integration*: Access and analyze NASA's tweets stored in an SQLite database.
- *Engagement Metrics Calculation*: Compute metrics such as likes, replies, retweets, and total engagement.
- *Comparative Insights*: Generate quantitative and qualitative insights to compare post performance.
- *Memory-Driven Conversations*: Retain chat history for continuous, context-aware interactions.

## Table Structure
The SQL database (tweets.db) contains a single table nasa_tweets with the following columns:

| Column         | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| content      | TEXT    | The content of the tweet.                        |
| likeCount    | INTEGER | Number of likes the tweet received.              |
| quoteCount   | INTEGER | Number of quotes the tweet received.             |
| replyCount   | INTEGER | Number of replies to the tweet.                  |
| retweetCount | INTEGER | Number of retweets the tweet received.           |
| url          | TEXT    | URL to the tweet.                                |
| post_type    | TEXT    | Type of post (Text, Image, Video, Gif).          |
| date         | TEXT    | Date the tweet was posted (dd/mm/yyyy).          |
| time         | TEXT    | Time the tweet was posted (hh:mm:ss).            |

## Getting Started

### Prerequisites
- Python 3.8+
- SQLite database (tweets.db)
- OpenAI API Key

### Installation
1. *Clone the Repository*:
    bash
    git clone https://github.com/your-repo/social-media-manager.git
    cd social-media-manager
    

2. *Install Dependencies*:
    bash
    pip install -r requirements.txt
    

3. *Set Up Environment Variables*:
    Create a .env file in the root directory:
    env
    OPENAI_API_KEY=your_openai_api_key
    

4. *Prepare the Database*:
    Ensure the tweets.db file is placed in the root directory. Verify the nasa_tweets table structure matches the schema described above.

5. *Run the Application*:
    bash
    streamlit run app.py
    

### Usage
1. Open the application in your web browser (default: http://localhost:8501).
2. Interact with the chat interface to ask questions like:
   - "What is the average engagement for video posts?"
   - "Compare the total engagement for text and image posts."
   - "Which type of post has the highest number of likes on average?"
3. The agent will query the database and return insightful responses based on the data.

### Example Queries
- *Metrics Calculation*:
  - "Calculate the total engagement for all video posts."
  - "What is the average number of retweets for text posts?"
- *Insights Generation*:
  - "Generate insights comparing engagement across all post types."
  - "Which post type performs better: images or videos?"

## Project Structure
├── app.py                 # Main Streamlit application 
├── prompt.txt             # System prompt for LangChain 
├── tweets.db              # SQLite database containing NASA's tweets 
├── requirements.txt       # Python dependencies 
├── .env                   # Environment variables 
└── README.md              # Project documentation

## Acknowledgments
- [LangChain](https://github.com/langchain-ai/langchain) for the conversational AI framework.
- [Streamlit](https://streamlit.io/) for building an interactive web app.
