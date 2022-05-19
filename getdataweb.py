import os

os.system("cls")

from urllib.request import urlopen
url = "https://www.kemkes.go.id/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")


print(len(html))

idx = html.find('Positif')
print(idx)
startP = idx + 68
endP   = startP + 9
akumulasiPositif = (html[startP:endP])

print("Akumulasi Positif hingga saat ini adalah "+akumulasiPositif)
