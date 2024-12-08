import matplotlib.pyplot as plt
import seaborn as sns

# Sentiment Distribution (Pie Chart)
sentiment_counts = df['Sentiment'].value_counts()
labels = ['Positive', 'Negative', 'Neutral']
colors = ['#66b3ff', '#ff6666', '#99ff99']

plt.figure(figsize=(14, 7))

# Pie Chart
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.pie(sentiment_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=(0.1, 0, 0))
plt.title('Sentiment Distribution in Reddit Posts')
plt.axis('equal')

# Top 10 Most Mentioned Stocks (Bar Chart)
stock_mentions = []
stock_tickers = ['TSLA', 'AAPL', 'AMZN', 'GOOGL', 'MSFT', 'META', 'NVDA', 'NFLX']

for title in df['Title']:
    for ticker in stock_tickers:
        if ticker in title:
            stock_mentions.append(ticker)

stock_mentions_df = pd.DataFrame(stock_mentions, columns=['Stock'])
stock_counts = stock_mentions_df['Stock'].value_counts()

plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
sns.barplot(x=stock_counts.index, y=stock_counts.values, palette='viridis')
plt.title('Top 10 Most Mentioned Stocks in Reddit Posts')
plt.xlabel('Stock Ticker')
plt.ylabel('Mention Count')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
