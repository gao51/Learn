from AMS.Driver import driver
i = 753732

url = 'https://www.xxbiquge.com/77_77665/' + str(i) + '.html'
driver = driver(url)
x = driver.find_element_by_xpath("//*[@id=\"content\"]")
print(x)