from time import sleep
from dotenv import load_dotenv
from os import getenv
from scraper.utils import fetch, parse, get_all_projects
import asyncio
from  scraper.db import  ConnectDB,logging

load_dotenv()

url = getenv("MOSTAQL_URL")

async def main():
    for i in range(1,36):
        db_con = ConnectDB()
        html = await fetch(url+str(i))
        result = parse(html)
        allData = get_all_projects(result)
        for item in allData:
            db_con.insert_in_db(item)
        db_con.close()
        logging.info("============="+str(i))
        print("=============",i)
        sleep(11)




if __name__ == '__main__':
    asyncio.run(main())


