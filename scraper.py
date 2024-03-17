import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
indeedURL = "https://au.indeed.com/?r=us"
authURL = "https://auth0.com/docs/authenticate/protocols/openid-connect-protocol"
page = requests.get(URL)
# print(page.text)
# print(page.cookies)
# print(page.raw)
soup = BeautifulSoup(page.content, "html.parser")

# finding element with id "ResultsContainer"
results = soup.find(id="ResultsContainer")
# print(results.prettify())

#finding elements by className
job_elements = results.find_all("div", class_="card-content")


# iterating through job_elements
# for job_element in job_elements:
#     # print(job_element, end="\n"*2)
#     # picking up child elements of each job posting
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()


# filtering out developer jobs
developer_jobs = results.find_all(
    "h2", string=lambda text: "developer" in text.lower() # here, we are passing lambda function as str. It converts the string to lowercase.
)

# stepping over the DOM ladder to get parent element of h2 which contains the Developer job title
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in developer_jobs
]

for job in python_job_elements:
    job_title = job.find('h2', class_="title")
    location_title = job.find('p', class_="location")
    company_title = job.find('h3', class_="company")
    print(job_title.text)
    print(location_title.text.strip())
    print(company_title.text.strip())
    print()