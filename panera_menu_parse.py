import urllib2
from bs4 import BeautifulSoup
def get_html(url):
    headers = {'User-Agent' : 'Mozilla/5.0'}
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

def find_menu_links():
    list_items = []
    key = "href"
    mya = soup.findAll("a")
    for a in mya:
        if a.has_attr(key):
            if 'menu-categories' in str(a[key]):
                list_items.append(a[key])
    return list_items

def find_links(key, attr):
    list_items = []
    items = soup.findAll(key)
    for i in items:
        if i.has_attr(attr):
            if str(i[attr]).startswith('#') and (str(i[attr]) != '#') \
            and (str(i[attr]) != '#navback') :
                list_items.append(i[attr])
    return list_items

def get_nutrition(url):
    print "get_nutrition(url) = " + url
    soup = get_html(url)
    #items = soup.findAll(lambda tag: tag.name == 'div' and tag.get('class') == ['item-content'])
    items = soup.find('div', attrs = {'class', 'two-col ingredients'})
    print items

    #print items[0].find("div", {'class' : 'two-col ingredients'}).text.strip()


root = "https://www.panerabread.com/"
soup = get_html(root)
links = find_menu_links()

# for link in links:
#     soup = get_html(root + link)
#     menu_items = find_links("a", "href")
#     for item in menu_items:
#         print root + link + item
#         #get_nutrition(root + link + item)


for link in links:
    soup = get_html(root + link)
    articles = soup.findAll('article', attrs = {'class' : 'one-column'})
    for a in articles:
        anchors = a.findAll('a')
        for n in anchors:
            if str(n['href']).startswith('#') and (str(n['href']) != '#') \
            and (str(n['href']) != '#navback'):
                print n['href']
        x = a.find('div', attrs = {'class' : 'two-col ingredients'})
        if x != None:
            print x.text.encode('utf-8').strip()
        #print a.findAll('a')[]
        print "\n\n"
#menu = find_links("a", "href")
#print "processing " + root + links[1] + menu[2]
#get_nutrition(root + links[1] + menu[2])

# for link in links:
#     soup = get_html(root + link)
#     menu = find_links("a", "href")
#     for m in menu:
#         print "!!!!!! NUTRITION FACTS FOR " + m + "!!!!!!!!!!!!!!!"
#         #soup = get_html(root + link + m)
#         get_nutrition(root + link + m)
