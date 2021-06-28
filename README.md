# Partisan News Viewer

This tool aims to create a news feed from sources at different points on the idealogical spectrum. The ratings used to determine these groupings and ordering of bias are pulled from Ad Fontes Media’s Bias Chart. These ratings do not reflect my own beliefs and are the result of work done by the independent group with describes itself as “a public benefit corporation with a mission to make news consumers smarter and news media better”. This project uses these ratings to attempt to show the extent of the informational divide that exists between partisan media outlets. 

## Installation

1. Clone the repo from GitHub.

```bash
git clone https://github.com/toehmler/news
```

2. Register for an account with [Datanews](datanews.io) to get an API key. Store this key in `server/.env` using the following format.

```
DATANEWS_API_KEY=[your api key]
```

3. Install the required python dependecies and start the flask server (will start the backend on port 5000). 

```bash
pip install -r requirements.txt
cd server && python app.py
```

4. Install the required node depedencies and start the frontend client (will start the client on port 8080)

```bash
cd client
npm install && npm run server
```

### Optional: Re-scrape sources and favicon
Included in this repo is a source list `sources_final.csv` that is used by the backend by default to determine which sources / websites should be fetched from using the Datanews API. To generate this source list on your own and re-run the scraping procedure, run the following:

```bash
python setup.py
python scrape_icons.py
python fix_icons.py
```

This will parse the media bias rating from Ad Fontes, then download a favicon for each source and lastly append the correct local path for each favicon to the final sources list.










