import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import re
import pandas as pd
import pdb

def scrap_site(url):
	cj = cookielib.CookieJar()
	br = mechanize.Browser()
	br.set_cookiejar(cj)

	br.open("https://www.linkedin.com/uas/login")
	br.select_form(nr=0)
	br.form['login'] = 'sanjay.bont@gmail.com'
	br.form['password'] = 'google123'
	br.submit()

	data = br.open(url).read()
	return data

url = "https://www.linkedin.com/profile/view?id=ADEAAAGgjq0BEloiTY5oMduiEXOLC1KpTgQJ7eQ&authType=OUT_OF_NETWORK&authToken=3b02&locale=en_US&srchid=4376043"
response = scrap_site(url)
print response