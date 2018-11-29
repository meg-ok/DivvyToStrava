import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

#Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling its session
br.open('https://www.divvybikes.com/login')

# View available forms
#for f in br.forms():
#    print f

# Select the first form (I think this will be the login username)
br.select_form(nr=0)

# User credentials
br.form['subscriberUsername'] = 'USERNAME'
br.form['subscriberPassword'] = 'PASSWORD'

# Login
br.submit()

print(br.open('https://www.divvybikes.com/account/trips').read())

