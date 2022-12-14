import mechanize 
from bsd import BeautifulSoup 

url = "https://www.findandtrace.com/trace-mobile-number-location"

brow = mechanize.Browser()  # you can even use salenium
brow.set_handle_robots(False)

# we have make it as false because some webiste doesn't allow us to scrap date
# so if our script founds that(robot.txt) file it will just ignore that and we will be continue using 
# our scrapping

brow.open(url)
brow.select_form(name="trace") 
brow['mobilenumber'] = str(input("Enter the mobile number : ")) # give your mobile number

# it will search for almost all the website except for which haven't registered anywhere or that data is explored

result =brow.submit() # we will record our response in result

soup = BeutifulSoup(result.read(),'html.parser')
table_extr = soup.find_all('table',close_ = 'shop_table')

data_extracted = table_extr[0].find('tfoot')
count = 0
for tr in data_extracted:
  count+ =1
  if count in (1,4,6,8):
    continue
  th = tr.find('th')
  td = tr.find('td')
  print(th.text,td.text)
  
  
data_extracted = table_extr[1].find('tfoot')
count = 0
for tr in data_extracted:
  count+ =1
  if count in (2,8,10,12,14,16,20,22,24,26):
    th = tr.find('th')
    td = tr.find('td')
    print(th.text,td.text)