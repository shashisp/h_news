from django.core.management.base import BaseCommand
import requests
import datetime
from bs4 import BeautifulSoup
from news.models import Article

class Command(BaseCommand):
  args = 'Arguments is not needed'
  help = 'Custom Command to populate data'
 
  def handle(self, *args, **options):

  	for page in range(1, 4):

	    html = requests.get('https://news.ycombinator.com/news?p='+str(page)).text

	    soup = BeautifulSoup(html)

	    main_table = soup.find("table")

	    articles = main_table.findAll("table")[1]

	    rows = articles.findAll("tr")

	    for row_num in range(0, len(rows)-3, 3):

	    	main_info = rows[row_num].findAll("td")
	    	count_info = rows[row_num + 1]

	    	article = { "url": main_info[2].find("a")["href"], "title": main_info[2].find("a").string}
	    	#remove pull stop at the tail
	    	article['rank'] = int(main_info[0].string[:1])
	    
	    	#if no comments
	    	try:
	    		article['comments'] = int(count_info.findAll("a")[2].string.split()[0])
	    	except Exception:
	    		article['comments'] = 0

	    	try:
	    		article['posted_on'] =  count_info.findAll("a")[1].string
	    	except Exception:
	    		continue


	    	#convert time to datetime format using timedelta 
	    	if article['posted_on']:
	    		s = article['posted_on']
	    		value, unit, _ = s.split()
	    		unit = str(unit)
	    		if unit == "hour":
	    			unit = "hours"
	    		elif unit == "day":
	    			unit = "days"
	    		elif unit == "minute":
	    			unit = "minutes"
	    		dt = datetime.timedelta(**{unit: float(value)})
	    		past_time = datetime.datetime.now() - dt

	    	article['hn_id'] = int(count_info.findAll('a')[2]['href'][8:])
	    	article['up_votes'] = int(count_info.findAll('span')[0].string.split()[0])
	    	article['hn_url'] = 'https://news.ycombinator.com/item?id='+str(article['hn_id'])
	    	# import ipdb; ipdb.set_trace()
	    	if not Article.objects.filter(hn_id=article['hn_id']).exists():
	        	Article.objects.get_or_create(title=article['title'], hn_id=article['hn_id'],
	        	 url=article['url'], hn_url=article['hn_url'],
	        	 posted_on=past_time, 
	        	 up_votes=article['up_votes'], 
	        	 comments=article['comments'],
	        	 rank=article['rank'])
	        	print "news created"
	        else:
	        	Article.objects.filter(hn_id=article['hn_id']).update(
	        		up_votes=article['up_votes'],
	        		comments=article['comments'],
	        		rank=article['rank'])
	        	print "news updated"
