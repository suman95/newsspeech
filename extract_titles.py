## Extracting different news items for different section
## Current program uses Google RSS feeds only
import feedparser

def extract_titles(url):
	# url="https://news.google.com/news/rss/headlines/section/topic/BUSINESS.en_in/Business?ned=in&hl=en-IN"
	titles = []
	feed = feedparser.parse(url)
	for item in feed["items"]:
		titles.append(item['title'])
	return titles

# function returns the RSS URL for different section
def return_url(section):
	# url="https://news.google.com/?output=rss"
	return {
			'sports':"https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN",
			'business':"https://news.google.com/news/rss/headlines/section/topic/BUSINESS.en_in/Business?ned=in&hl=en-IN",
			'india':"https://news.google.com/news/rss/headlines/section/topic/NATION.en_in/India?ned=in&hl=en-IN",
			'world':"https://news.google.com/news/rss/headlines/section/topic/WORLD.en_in/World?ned=in&hl=en-IN",
			'entertainment':"https://news.google.com/news/rss/headlines/section/topic/ENTERTAINMENT.en_in/Entertainment?ned=in&hl=en-IN",
			'education':'https://news.google.com/news/rss/headlines/section/q/Education%20and%20Technology/Education%20and%20Technology?ned=in&hl=en-IN'
			'topstories':'https://news.google.com/?output=rss'
	}[section]

def return_news_for(section):
	return extract_titles(return_url(section))


## for testing purpose
if __name__ == '__main__':
	print(return_news_for('business'))