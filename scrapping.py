import bs4 as bs
import urllib.request
import pandas as pd
import numpy as np

def scrap_insee(source, output):
    source = urllib.request.urlopen(source).read()
    soup = bs.BeautifulSoup(source,'lxml')
    h3s = soup.find_all('h3')
    titles = []
    for i in h3s:
        try:
            titles.append(str(i).split('</span>')[1].split('</h3>')[0].replace('\n',''))
        except:
            print('end of file')
    titles = np.unique(titles)
    table = soup.find_all('table')
    for i in range(len(titles)):
        df = pd.read_html(str(table))[i]
        df.to_csv(output+'/'+titles[i]+'.csv', index=False)
        
scrap_insee('https://www.insee.fr/fr/statistiques/2011101?geo=DEP-40#consulter-sommaire', 'data_scrapped')