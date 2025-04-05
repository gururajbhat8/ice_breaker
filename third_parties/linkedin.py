import os
import requests
from dotenv import load_dotenv 

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str , mock: bool=False):

    if mock:
        linkedin_profile_url = "https://gist.github.com/gururajbhat8/14369d42dfc8333cbe508ed229e81ba7"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey" : os.environ["SCRAPIN_API_KEY"],
            "linkedinurl" : linkedin_profile_url
        }

        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )

        data = response.json("person")

        data = {
            k : v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["certifications"]
        }

        return data 



if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
        linkedin_profile_url= "https://www.linkedin.com/in/harrison-chase-961287118/",
        mock=True
        ),
    )