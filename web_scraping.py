import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import requests_html

job_titles = []
company_names = []
locations = []
job_skills = []
links = []
salaries = []
job_requirements = []
date = []
# switch pages
page_num = 0
while True:
    # use requests to bring the url
    result = requests.get(
        f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")

    # save page content/markup
    src = result.content

    # create soup object to parse content
    soup = BeautifulSoup(src, "lxml")

    # find the elements containing info we need
    # job titles, job skills, company name, location name, date
    jobs_num = int(soup.find("strong").text)
    job_title = soup.find_all("h2", {"class": "css-m604qf"})
    company_name = soup.find_all("a", {"class": "css-17s97q8"})
    location = soup.find_all("span", {"class": "css-5wys0k"})
    job_skill = soup.find_all("div", {"class": "css-y4udm8"})
    posted_old = soup.find_all("div", {"class": "css-do6t5g"})
    posted_new = soup.find_all("div", {"class": "css-4c4ojb"})
    posted = [*posted_new, *posted_old]

    # loop over returned lists to extract needed info(text) into other lists
    for i in range(len(job_title)):
        job_titles.append(job_title[i].text)
        links.append(job_title[i].find("a").attrs["href"])
        company_names.append(company_name[i].text)
        locations.append(location[i].text)
        job_skills.append(job_skill[i].find("div", {"class": None}).text)
        date.append(posted[i].text)

    # max jobs in a page is 15
    page_limit = jobs_num // 15
    if (jobs_num % 15) != 0:
        page_limit += 1

    page_num += 1

    if page_num > page_limit:
        break

try:
    # loop over the links so you can go to them and get needed information
    for link in links:
        # prepare the absolute link
        url = "https://wuzzuf.net" + link
        # prepare a session and render it so the javascript content load
        session = requests_html.HTMLSession()
        r = session.get(url)
        r.html.render(sleep=.5, keep_page=True, scrolldown=1)
        # get the salary which is the forth span with class css-47jx3m in the page
        salary = r.html.find("span.css-47jx3m")
        item = salary[3]
        salaries.append(item.text)
        # get job requirements
        job_requirement = r.html.find("div.css-1t5f0fr")
        for item in job_requirement:
            job_requirements.append(item.text)
except:
    print("error occurred")

# create csv file and fill it with values
with open(r"C:\Users\HP\Desktop\jobresults.csv", 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["job title", "date", "company name", "location",
                    "job skill", "salaries", "job Requirements"])
    file_list = [job_titles, date, company_names, locations,
                 job_skills, salaries, job_requirements]
    exported = zip_longest(*file_list)
    writer.writerows(exported)
