# 1st step install and import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import re

job_title = []
company_name = []
location = []
skills = []
links = []
salary = []
responsibilities=[]
baseurl="https://wuzzuf.net"

# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


# 2nd step use requeststo fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
# 3rd step save page content/markup
src = result.content
# print(src)
# 4th step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
# print(soup)
# 5th step find the elements containing info we need
# __ job titles ,job skils, company names , location
# first attribute html tag(h2) second attribute {class:css-m604qf}

jobs_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
company_location = soup.find_all("span", {"class": "css-5wys0k"})
job_skils = soup.find_all("div", {"class": "css-y4udm8"})
# print(job_skils)
# 6th step loop over retuened lists to extract needed info into other lists
for i in range(len(jobs_titles)):
    job_title.append(jobs_titles[i].text)
    """
    url_to_scrape = "https://wuzzuf.net/search/jobs/?q=python&a=hpb"
    html_document = getHTMLdocument(url_to_scrape)
    soup2 = BeautifulSoup(html_document, 'html.parser')
"""
    links.append(baseurl+
                 jobs_titles[i].find("a").attrs['href']) # will get the link of the job to scrap the requirements
    company_name.append(company_names[i].text)
    location.append(company_location[i].text)
    skills.append(job_skils[i].text)
"""
for link in soup.find_all('a',
                          attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href'))   # strip to remove whitespaces
"""
for link in links:
    result=requests.get(link)
    src=result.content
    soup=BeautifulSoup(src,"lxml")
    salaries=soup.find("span",{"class":"css-4xky9y"})
    salary.append(salaries)


print(links)
print(responsibilities)


# print(job_title,"\n",company_name,"\n",location,"\n",skills)
# 7th step create csv file and fill it with values
file_list = [job_title, company_name, location, skills, links, salary]
exported = zip_longest(*file_list)
"""
x=[1,2,3]
y=["x","y","z"]
z=[x,y]
zip_longest(*z)---->[[1,2,3],["a","b","c"]]
---> [1,a],[2,b],[3,c]
 * to unpacking the values لتفريغ  المحتوى
"""
with open("E:\programming\python\web scraping/jobs.csv", "w") as myfile:
    wr = csv.writer(myfile)  # wr=writer
    # make head row inside csv file
    wr.writerow(["Job Title", "Company Name", "Location", "Skills", "Links", "salary"])  # writerow take list value
    wr.writerows(exported)  # writerows stake list value
