# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.x-rates.com/calculator/?from=USD&to=TRY&amount=1'
# response = requests.get(url)
# soup = BeautifulSoup(response.text , 'html.parser')
#
# trail = soup.find('span', class_='ccOutputTrail')
# if trail:
#     number = trail.previous_sibling.strip()
#     currency = trail.get_text(strip=True)
#     print(f'1 USD = {number}{currency}')
# else:
#     print(f'could not find course ')
