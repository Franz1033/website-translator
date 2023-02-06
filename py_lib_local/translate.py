import json
import requests
from bs4 import BeautifulSoup

def translate_webpage(url, api_key, target_language='hi'):
    # Configure site url
    SITE_URL = 'https://website-translator.vercel.app'

   # URL for the Google Translate API
    translate_url = 'https://translation.googleapis.com/language/translate/v2'

    # Get HTML content of the URL
    html = requests.get(url).text

    # Configure the payload for the request
    payload = {
        'q': html, # The HTML content to be translated
        'target': target_language, # The target language to translate to
        'format': 'html', # Format of the content being translated
        'key': api_key # API Key for authentication
    }

    # Send POST request to the API
    response = requests.post(translate_url, data=payload)

    # Load the JSON response from the API
    response_dict = json.loads(response.text)

    # Extract the translated HTML from the response
    translated_html = response_dict['data']['translations'][0]['translatedText']

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(translated_html, 'html.parser')

    # Get all anchor elements
    anchor_elements = soup.findAll('a')

    # Replace the href path for each anchor element
    for anchor_element in anchor_elements:
        try:
            anchor_element["href"] = SITE_URL + str(anchor_element["href"].replace("?#main-content", "")) + '/index.html'
        except KeyError:
            pass

    # Return the prettified HTML
    return soup.prettify()

def main():
    pass

if __name__ == '__main__':
    main()
