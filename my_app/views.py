from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . models import Search
# Create your views here.

BASE_WEBSITE_URL = 'https://delhi.craigslist.org/search/bbb?query={}'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    final_url = BASE_WEBSITE_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('a', {'class': 'result-title'})
    post_listings = soup.find_all('li', {'class': 'result-row'})
    final_postings = []

    for post in post_listings:
        post_title = post.find('a', {'class': 'result-title'}).text
        post_url = post.find('a').get('href')

        final_postings.append((post_title, post_url))

    print(final_postings)
    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
        'title': 'Search'
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
