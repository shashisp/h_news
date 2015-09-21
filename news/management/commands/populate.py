from django.core.management.base import BaseCommand
import requests
import datetime
from bs4 import BeautifulSoup
from news.models import Article

class Command(BaseCommand):
  args = 'Arguments is not needed'
  help = 'Custom Command to populate data'
 
  def handle(self, *args, **options):
      html = requests.get('https://news.ycombinator.com/').text

      soup = BeautifulSoup(html, "lxml")

      for row in soup.find_all('tr')[2:]:
          if len(row.find_all('td')) == 3:
            # import ipdb; ipdb.set_trace()
            print row