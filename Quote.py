# import  requests
# from bs4 import BeautifulSoup
#
# URL = 'https://quotes.toscrape.com'
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, 'html.parser')
#
#
# Quotes = soup.find_all('div', class_='quote')
# for Quote in Quotes:
#     text = Quote.find("span", class_='text').get_text()
#     author = Quote.find('small', class_='author').get_text()
#     print(f'Quote: {text}')
#     print(f'Author: {author} \n')




