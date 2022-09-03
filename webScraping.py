from time import sleep
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import chromedriver_autoinstaller
import helium

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
try:
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

    chromedriver_autoinstaller.install()
    # loop over the links so you can go to them and get needed information
    for link in links:
        # prepare the absolute link
        url = "https://wuzzuf.net" + link
        # prepare a session and render it so the javascript content load
        browser = helium.start_chrome(url, headless=True)
        sleep(1)
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # get the salary which is the forth span with class css-47jx3m in the page
        salary = soup.find("span", {"class": "css-47jx3m"})
        salary = salary.find_next("span", {"class": "css-47jx3m"})
        salary = salary.find_next("span", {"class": "css-47jx3m"})
        salary = salary.find_next("span", {"class": "css-47jx3m"})
        salaries.append(salary.text)
        # get job requirements
        job_requirement = soup.find("div", {"class": "css-1t5f0fr"})
        job_requirements.append(job_requirement.text)
except Exception as links_error:
    print(links_error)

# create csv file and fill it with values
with open(r"C:\Users\HP\Desktop\jobresults.csv", 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["job title", "date", "company name", "location",
                    "job skill", "salaries", "job Requirements"])
    file_list = [job_titles, date, company_names, locations,
                 job_skills, salaries, job_requirements]
    exported = zip_longest(*file_list)
    writer.writerows(exported)
