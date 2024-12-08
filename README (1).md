          STOCK MOVEMENT ANALYSIS USING REDDIT DATA



𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧

The stock market is influenced not only by financial data but also by public sentiment and discussion. This project explores the potential of social media, particularly Reddit, to forecast stock trends by analyzing user-generated content. Using the r/stocks subreddit, I scraped data, extracted sentiment insights, and created a foundation for predicting stock movements.

𝐊𝐞𝐲 𝐇𝐢𝐠𝐡𝐥𝐢𝐠𝐡𝐭𝐬

1️⃣ Scraped 500 top posts from r/stocks to capture discussions on stock trends.
2️⃣ Leveraged NLP sentiment analysis to quantify public sentiment around specific stocks.
3️⃣ Prepared the dataset (refined_reddit_data.csv) for machine    learning or statistical analysis.
4️⃣ Example insights include:
Most-discussed stocks.
Average sentiment of posts (positive, neutral, negative).


reddit PRAW API

## Run Locally

Clone the project

```bash
  git clone https://github.com/Izzxth/Stock_prediction.git
  
```


## Requirements

Python 3.x
pip (Python package installer)
Dependencies (can be installed via requirements.txt)


𝐓𝐨𝐨𝐥𝐬 & 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬
1. Python: Programming language for scraping, analysis, and data handling.
2. PRAW: Efficiently fetch structured data from Reddit.
3. NLTK: Natural Language Toolkit for sentiment analysis.
4. Pandas: Data manipulation and storage.
5. Jupyter Notebooks: For testing and documenting the workflow.
## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Authors

Izzath Fathima (https://github.com/Izzxth)
mail: izzu0512@gmail.com
## Deployment

1. Clone the repository:
git clone <repo-link>
cd <repo-folder>

2. Install dependencies:
pip install praw pandas nltk

3. Replace the placeholders (client_id, client_secret, user_agent) with your Reddit API credentials.

4. Run the script:
python reddit_scraper.py

5. Output: A refined CSV file (refined_reddit_data.csv) and top sentiment insights printed to the console.



## Approach
𝐀𝐩𝐩𝐫𝐨𝐚𝐜𝐡

1. Data Collection
Scraped posts from the r/stocks subreddit using PRAW.
Captured the following fields:
Title: Post title (key discussion point).
Score: Upvote count as a popularity metric.
Comments: Number of comments as an engagement metric.
Body: Full text of the post.
2. Data Cleaning
Removed duplicates and irrelevant posts.
Ensured all fields were populated (handled missing values).
3. Sentiment Analysis
Analyzed the sentiment of each post title using NLTK’s VADER Sentiment Analyzer.
Generated a compound sentiment score for each post:
Positive values indicate optimism.
Negative values indicate pessimism.
Scores close to zero suggest neutrality.
