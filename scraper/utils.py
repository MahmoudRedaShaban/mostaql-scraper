from os import getenv
import httpx
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


async  def fetch(url):
    headers = {"User-Agent": getenv('Headers')}
    async  with httpx.AsyncClient() as Client:
        response = await  Client.get(url,headers=headers)
        return response.text



def parse(html):
    return BeautifulSoup(html ,'html.parser')



def get_all_projects(soup):
    return [ handel_item_project(project) for project in soup.select('.project-row ')]

def handel_item_project(soup_project):
    title_elem = soup_project.select_one('.card-title_wrapper > div.card--title > h2')
    meta_elem = soup_project.select_one('div.card-title_wrapper > div.card--title > ul > li:nth-child(1) > bdi')
    desc_elem = soup_project.select_one('.project__brief')
    link_elem = soup_project.find('a', href=True)

    title = title_elem.text.strip() if title_elem else ''
    meta_project = meta_elem.text.strip() if meta_elem else ''
    desc_project = desc_elem.text.strip() if desc_elem else ''
    link = link_elem['href'] if link_elem else ''

    return {
        'title': title,
        'meta': meta_project,
        'description': desc_project,
        'link': link
    }
