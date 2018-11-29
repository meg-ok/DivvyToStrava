import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text


def yes():
    print '0'

def DoUpload( minutes, seconds, distance, start_date, time_of_day ):
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
  br.open('https://www.strava.com/login')

  # View available forms
  #for f in br.forms():
  #    print f

  # Select the first form (I think this will be the login username)
  br.select_form(nr=0)

  # User credentials
  br.form['email'] = 'EMAIL'
  br.form['password'] = 'PASSWORD'

  # Login
  br.submit()

  #print(br.open('https://www.strava.com/upload/manual').read())
  br.open('https://www.strava.com/upload/manual')

# View available forms
#for f in br.forms():
#    print f
# Think it's the first (only?) form on page
  br.select_form(nr=0)

# Activity name
  br.form['activity[name]'] = 'Divvy Bike Ride Auto Upload'

# Commute? Let's say yes
#br.form['activity[commute]'] = '1'
# XXX multiple forms called by this name! a checkbox, and hidden

# Hours, minutes, and seconds
  br.form['activity[elapsed_time_hours]'] = '0'
  br.form['activity[elapsed_time_minutes]'] = minutes
  br.form['activity[elapsed_time_seconds]'] = seconds

# Distance (in miles?)
  br.form['activity[distance]'] = distance#'3.3'

# Date
  br.form['activity[start_date]'] = start_date#'08/29/2015'

# Time Started
  br.form['activity[start_time_of_day]'] = time_of_day#'04:38 pm' # or '04:38 PM'

  print "date", start_date
  print "time of day", time_of_day
  print "minutes ", minutes
  print "seconds ", seconds

  br.submit()

#yes()


