import requests
from bs4 import BeautifulSoup
import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

response = requests.get(url='https://steamdb.info/', headers=headers)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')


def has_class_and_data_cache(tag):
    return tag.has_attr('class') and tag.has_attr('data-cache')


games_tags = soup.find_all(has_class_and_data_cache)

with open('scrap_data_most_played_games.csv', 'w', newline='') as csvfile:
    fieldnames = ['Game', 'Players now', 'Peak Today']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for game in games_tags[1:16]:
        list_data = ((game.get_text().replace('\n\n\n\n\n\n\n', '')).split('\n'))
        writer.writerow({'Game': list_data[0], "Players now": list_data[2], "Peak Today": list_data[3]})
    csvfile.close()


with open('scrap_data_popular_relases.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['Game', 'Peak Today', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for game in games_tags[34:46]:
        list_data = ((game.get_text().replace('\n\n\n\n\n\n\n', '')).split('\n'))
        writer.writerow({'Game': list_data[6], "Peak Today": list_data[7], "Price": list_data[8]})
    csvfile.close()