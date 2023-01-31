from bs4 import BeautifulSoup
bilancio = open('bilancio_test.xml', 'r')
soup = BeautifulSoup(bilancio

def print_value(soup, el):
    print(int(soup.find(el).text))

print_value(soup, 'itcc-ci:utileperditaesercizio')
print_value(soup, 'itcc-ci:totaleattivo')
print_value(soup, 'itcc-ci:totalepassivo')

### analisi conto corrente

---------

import csv
import numpy as np
from scipy.stats import tmean, tstd, tmin, tmax, norm, kurtosis, skew

conto = open('Transazioni_Azienda ABC - Foglio1.csv', 'r')
reader = csv.reader(conto)
first = True
ls = []
for row in reader:
    if first:
        first = False
        continue
    v = row[2]
    v = v.replace('€', '').replace('.', '').replace(',', '.').replace(' ', '')
    ls.append(float(v))
    
print(ls)

aux = []
for i in range(0, len(ls)):
    aux.append(sum(ls[:i]))
    
print(tmean(aux))
print(tstd(aux))
print(tmin(aux))
print(tmax(aux))
print(kurtosis(aux))
print(skew(aux))
