import requests
import pandas as pd
import fastparquet
import duckdb
from datetime import date
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.6',
    'content-type': 'application/json',
    'priority': 'u=1, i',
    'referer': 'https://jobnet.dk/find-job?searchString=Data+analyse',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Brave";v="157", "Chromium";v="157"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36',
    'x-csrf': '1',
}

queries = [
    "Data analyse",
    "studentermedhjælper data",
    "studentermedhjælper analyse",
    "student data analyst",
    "junior data analyst",
    "data intern",
    "junior Python",
    "data scientist",
    "data engineer",
    "business intelligence",
    "machine learning",
    "SQL",
]

for query in queries:
    params = {
        'resultsPerPage': '400',
        'pageNumber': 1,
        'orderType': 'BestMatch',
        'kmRadius': '50',
        'searchString': query,
    }

    response = requests.get('https://jobnet.dk/bff/FindJob/Search', params=params, headers=headers)
    data = response.json()
    ads = data["jobAds"]
    df = pd.DataFrame(ads)
    df["search_query"] = query
    df.to_parquet(f'job_market_analysis/raw_data/Jobnet_{query}_{date.today()}.parquet')   



