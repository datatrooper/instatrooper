from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
url = "https://fangj.github.io/friends/"
html = urlopen(url).read()
soup = BeautifulSoup(html)

refs = []
for a in soup.find_all('a', href=True):
    refs.append(a['href'])

character = []
line = []
for ref in refs:
    print(ref)
    url_e = url + ref
    html = urlopen(url_e).read()
    soup = BeautifulSoup(html)
    text = soup.get_text()
    lines = text.splitlines()
    dialogs = [s for s in lines if ":" in s]
    for d in dialogs:
        character.append(d.split(":")[0])
        line.append(d.split(":")[1])
    

df = pd.DataFrame({"Character": character, "Line":line})
df.to_csv("FriendsLines.csv", index=False)
print(df)