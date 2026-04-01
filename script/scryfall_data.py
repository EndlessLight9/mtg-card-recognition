import os
import requests
import pandas as pd
import time

from pathlib import Path

def fetch_scryfall_data(limit = 100):
    """
    Function to fetch card data from Scryfall API, process data and download card images.
    """
    # Requesting card API data from Scryfall
    url_bulk = "https://api.scryfall.com/bulk-data"

    headers = {
        "User-Agent": "AIProject/1.0",
        "Accept": "application/json"
    }
    response_bulk = requests.get(url_bulk, headers=headers)

    if response_bulk.status_code != 200:
        print(f"Connection error: {response_bulk.status_code}")
        print(f"Response: {response_bulk.text}")
    
    response_bulk = response_bulk.json()
    # searching for 'oracle_cards' which contains only 1 version of each card
    link_download_json = None
    for pack in response_bulk['data']:
        if pack['type'] == 'oracle_cards':
            link_download_json = pack['download_uri']
            break
    
    if not link_download_json:
        print("Could not find the oracle_cards data in the bulk data.")
        return
    
    #download json catalog
    raw_data = requests.get(link_download_json).json()

    #transforming json data into a pandas dataframe
    df = pd.DataFrame(raw_data)

    #since there are many cards, such as tokens, basic lands, that can have multiple versions, we will only keep those which column "image_uris" is unique
    valid_df = df.dropna(subset=['image_uris']).copy()

    #scryfall saves URL in a dictionary, we will only keep the normal image URL
    valid_df['image_url'] = valid_df['image_uris'].apply(lambda x: x.get('normal'))

    #remove any 'non' normal versions
    valid_df = valid_df.dropna(subset=['image_url'])

    #establish directory to save images
    root_dir = Path(__file__).resolve().parent.parent
    image_dir = root_dir / "scryfall_data"
    image_dir.mkdir(parents=True, exist_ok=True)

    #download images
    for index, row in valid_df.head(limit).iterrows():
        #some little preprocessing regarding card names to avoid issues with file naming
        clean_name = str(row['name']).replace("/", "_").replace(":", "").replace('"','')
        url_img = row['image_url']

        file_path = os.path.join(image_dir, f"{clean_name}.jpg")

        #only download image if file doesnt exist

        if not os.path.exists(file_path):
            try:
                img_bytes = requests.get(url_img).content
                with open(file_path, 'wb') as file:
                    file.write(img_bytes)
                print(f"[OK] Downloaded: {clean_name}")
            except Exception as e:
                print(f"[ERROR] Failed to download {clean_name}: {e}")
            time.sleep(0.1)  # Sleep to avoid hitting rate limits
        else:
            print(f"[SKIP] Already exists: {clean_name}")
    print("All images have been processed.")

if __name__ == "__main__":
    fetch_scryfall_data(limit = 100 )

