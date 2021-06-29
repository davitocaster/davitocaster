import requests
from bs4 import BeautifulSoup
import time

print(' ')
print('Maze SKU Search for Copping Brazil - by davitocaster')
print(' ')
time.sleep(1)

agent = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
sku_inicio = 4863118
sku_fim = 4863156
tenis = str(input('Modelo do tênis que deseja procurar: '))

for sku in range(sku_inicio, sku_fim):
  url = 'https://www.maze.com.br/produto/coppingbrazil/' + str(sku)

  r = requests.get(url, headers=agent)
  soup = BeautifulSoup(r.content, 'html.parser')
  product_name = soup.find('h1', class_='nomeProduto')

  if tenis in soup.prettify():
      print('PRODUTO ENCONTRADO:', product_name.text, '(Link:', url + ')')
  else:
      print('Código', sku, 'checado, nenhum resultado encontrado.')

time.sleep(3)
