# Website Translator
This program translates a website one level deep and automatically generates HTML files

## How to use:
1. Clone the repository to your local machine git clone `https://github.com/Franz1033/website-translator.git`
2. Before reconfiguring, first delete `data.csv` and `html` directory
3. Open `main.py` and plug in your own Google Cloud API key you can do so [here](https://cloud.google.com/translate)
4. Also set your target webpage url
5. Lastly, open the `py_lib_local` library then open `translate.py` and change `SITE_URL` to your own live website url, you could use [Vercel](https://vercel.com) for this
6. Finally, run the python project using `python3 main.py`

### To change target language:
On line 31 of `main.py` change the `'hi'` parameter inside the `translate_webpage()` function to other supported languages. See the list [here](https://cloud.google.com/translate/docs/languages) 
