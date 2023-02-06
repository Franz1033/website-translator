import os
import requests
from bs4 import BeautifulSoup
import csv

def scrape_webpage(url):

    headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}

    r = requests.get(url=url, headers=headers)
    # # Get raw HTML content
    # print(r.content)

    # Parse HTML content
    soup = BeautifulSoup(r.content, 'html.parser') 

    # List of all links from each anchor elemnt
    links = []

    # Find all anchor elements
    # Note: To look for specific element attrs use attrs = {'id':'example'} as argument
    anchor_elements = soup.findAll('a')

    # Iteratively append all href vals to the links lst
    for index, anchor_element in enumerate(anchor_elements):

        link = {}

        # Create ID & Links keys and plug-in their corresponding vals
        link[f"ID"] = index 
        link[f"Links"] = anchor_element.get("href")

        # Append this newly created dict to the links lst
        links.append(link)

    # Define the file path
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.csv')

    # Finally, create a csv file containing the ID and Links cols
    with open(file_path, 'w', newline='') as f:
        # Create a header
        w = csv.DictWriter(f, ['ID', "Links"])
        w.writeheader()
        for link in links:
            # Add each link as row
            w.writerow(link)

    # print("Task Completed!")

def main():
    pass

if __name__ == '__main__':
    main()    

'''
Note: Modify code accordingly based on the desired HTML element to be accessed. 
To do this, modify first line 21 before changing other codes in this program. 
'''



