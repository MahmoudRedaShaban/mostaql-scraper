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



