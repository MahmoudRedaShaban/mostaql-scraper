from dotenv import load_dotenv
from os import getenv
from scraper.utils import fetch,parse
import asyncio


load_dotenv()

url = getenv("MOSTAQL_URL")

async def main():
    html = await fetch(url)
    result = parse(html)
    print(result)



if __name__ == '__main__':
    asyncio.run(main())