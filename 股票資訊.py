from requests import get
from bs4 import BeautifulSoup

print('- 代表無資料')

link = 'https://tw.stock.yahoo.com'

html = get('https://tw.stock.yahoo.com/s/list.php?c=%AA%F7%BF%C4&rr=0.78878600%201553565438').text
soup = BeautifulSoup(html,'html.parser')

h = []


for name in soup.find_all('a'):
    h.append(name.get('href'))

h = [h for h in h if h[0:2] == '/q']



nh = [] # 股票網址

nnh = [] # 股票代號

lx = [] # 基本資料的股票網址

nnnh = []
for i in range(len(h)):
    nh.append(link+h[i])

for n in range(len(nh)):
    nnh.append(nh[n][-9:-5])

for i in range(len(nnh)):
    nlink = 'https://tw.stock.yahoo.com/d/s/company_'+nnh[i]+'.html'
    lx.append(nlink)

for i in range(len(nnh)):
    if nnh[i].isdigit() == False:
        nnh[i] = nnh[i - 1]

# -----------------------------------------------------------------------------------


for i in range(len(nnh)):
    html = get('https://tw.stock.yahoo.com/d/s/company_{}.html'.format(nnh[i])).text
    soup = BeautifulSoup(html,'html.parser')
    li = []
    for n1 in soup.find('td',width=83):
        li.append(n1)
    li2 = []
    for n2 in soup.find_all('td',{'align':'center'}):
        li2.append(n2.string)
    print('現金股利: {}, 股票股利: {}, 盈餘配股: {}, 網址: {}'.format(li2[3],li2[4],li2[5],lx[i]))
    print()
