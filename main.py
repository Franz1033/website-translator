import pandas as pd
import urllib.parse
from py_lib_local import scrape, translate, generate

def main():
    # Google Translate API Key
    API_KEY = 'AIzaSyA4NMeanx0Cx5rsVmqfuyW5Aqa_TafLs0s'

    # Webpage URL
    TARGET_URL = 'https://www.trilz.io'
    
    # Scrape webpage links
    scrape.scrape_webpage(TARGET_URL)

    # Read the data from the CSV file
    df = pd.read_csv('data.csv')

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Get the link from the 'Links' column
        link = row['Links']

        # Check if the link starts with a "/" character
        if link.startswith("/"):
            # If so, add the URL to the beginning of the link
            link = TARGET_URL + link

        # Check if the link starts with the URL
        if link.startswith(TARGET_URL):
            # If so, translate webpage
            translated_html = translate.translate_webpage(link, API_KEY, 'hi')

            # Define the file path
            file_path = urllib.parse.urlparse(link).path

            # Generate HTML file
            generate.generate_html(translated_html, file_path)
    
    print("Task Complated!")

if __name__ == '__main__':
    main()
