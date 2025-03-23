import feedparser
from bs4 import BeautifulSoup # type: ignore

# Google News RSS feed for Booz Allen Hamilton
rss_url = "https://news.google.com/rss/search?q=Booz+Allen+Hamilton"

# Parse the feed
feed = feedparser.parse(rss_url)

# Extract top 10 stories
news_items = []
for entry in feed.entries[:10]:
    title = entry.title
    link = entry.link
    published = entry.published
    summary = BeautifulSoup(entry.summary, "html.parser").get_text()
    news_items.append((title, link, published, summary))

# Create HTML content
html_content = "<h2>Booz Allen Hamilton in the News</h2><ul>"
for title, link, published, summary in news_items:
    html_content += f"<li><a href='{link}' target='_blank'><strong>{title}</strong></a><br><em>{published}</em><br>{summary}</li><br>"
html_content += "</ul>"

# Save to file
with open("bah_news_feed.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ News feed saved as 'bah_news_feed.html'")
