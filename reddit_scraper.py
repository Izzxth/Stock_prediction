import praw
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Install NLTK resources if not already done
nltk.download("vader_lexicon")

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Reddit API Credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",           # Replace with your client ID
    client_secret="YOUR_CLIENT_SECRET",   # Replace with your client secret
    user_agent="YOUR_USER_AGENT"          # Replace with your app name
)

# Scrape Data from r/stocks Subreddit
subreddit = reddit.subreddit("stocks")
posts = []
try:
    for post in subreddit.top(limit=500):  # Adjust limit if needed
        # Perform sentiment analysis on the title
        sentiment = sia.polarity_scores(post.title)
        posts.append([
            post.title,
            post.score,
            post.num_comments,
            post.selftext,
            sentiment["compound"]  # Use compound score for overall sentiment
        ])
except Exception as e:
    print(f"Error occurred: {e}")

# Create DataFrame
df = pd.DataFrame(posts, columns=["Title", "Score", "Comments", "Body", "Sentiment"])

# Save to CSV
output_file = "refined_reddit_data.csv"
df.to_csv(output_file, index=False)
print(f"Saved refined data to {output_file}")

# Display Summary
print("Top 5 Posts by Sentiment:")
print(df.nlargest(5, "Sentiment")[["Title", "Sentiment"]])

#Load data (Assuming refined_reddit_data.csv is loaded)
df = pd.read_csv('refined_reddit_data.csv')

#Feature Engineering
# Convert the 'Sentiment' column to numerical values: Positive = 1, Negative = 0, Neutral = 2
df['Sentiment'] = df['Sentiment'].map({'Positive': 1, 'Negative': 0, 'Neutral': 2})

# Convert text data into numerical features using TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust the number of features
X = vectorizer.fit_transform(df['Body'])

# Define the target variable
y = df['Sentiment']

#Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Evaluate the Model
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print("Classification Report:")
print(classification_report(y_test, y_pred))