import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),features="html.parser")
elems = exampleSoup.select('.slogan')
print(elems)
print(type(elems))
print(len(elems))

print(type(elems[0]))
print(elems[0].getText())

print(elems[0].attrs)


print("--------------nuevo testeo-------------")
print(elems)
print(str(elems[0]))
print(elems[0].attrs)




print("-------------- parafos-------------")


pElems = exampleSoup.select('p')

print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())




