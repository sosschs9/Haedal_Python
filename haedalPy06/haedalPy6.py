import bs4
import requests

headers = {
    'User-Agent': 'Not_Crawling X)'
}

response = requests.get('https://kin.naver.com/', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
lists = soup.select('.stats_ranking_area>.ranking_section>.ranking_list_area>ul>li')

with open('Q&A_rank.csv', 'w') as f:
    for data in lists:
        rank = data.select_one('span.no').text
        title = data.select_one('a.ranking_title').text
        f.write(f'{rank}위,{title}\n')