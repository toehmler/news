import csv
import datanews
import json
from datetime import datetime
import arrow
import os
from dotenv import load_dotenv

class source_map:
    def __init__(self, file_path='sources_final.csv'):
        load_dotenv()
        self.file_path = file_path
        self.left_sources = []
        self.right_sources = []
        self.radius = 1
        self.api_key= os.environ.get('DATANEWS_API_KEY')
        self.api_key = '0fraab4bvhzj7f59n3z6hds0f'
        self.datanews = datanews
        self.datanews.api_key = self.api_key
        self.left_articles, self.right_articles = self.seed_articles()

    # -77_results.json
    # 68

    def seed_articles(self):
        left_file = open('left_sample.json', 'r')
        left_data = json.load(left_file)
        left_file.close()
        right_file = open('right_sample.json', 'r')
        right_data = json.load(right_file)
        right_file.close()
        return left_data, right_data


    def load_sources(self):
        sources_file = open(self.file_path, encoding="utf-8")
        reader = csv.reader(sources_file)
        sources = [(row[0], row[1], float(row[3]), row[4]) for row in reader]
        L_s = [s for s in sources if s[2] < 0]
        R_s = [s for s in sources if s[2] > 0]
        L_s.sort(key=lambda tup: abs(tup[2]))
        R_s.sort(key=lambda tup: tup[2])
        self.left_sources = L_s
        self.right_sources = R_s
        sources_file.close()

    def fetch_sources(self, bias):
        if bias < 0:
            source_list = self.left_sources
        else:
            source_list = self.right_sources
        idx = int(abs(bias)/100 * len(source_list))
        results = [source_list[idx]]
        current_radius = 1
        while current_radius <= self.radius:
            if idx - current_radius >= 0:
                results.append(source_list[idx - current_radius])
            if idx + current_radius < len(source_list):
                results.append(source_list[idx + current_radius])
            current_radius += 1
        return results

    def format_url(self, url):
        start = url.find('/')
        if url[start+2:start+6] == 'www.':
            start += 6
        else:
            start += 2
        fmt_url = url[start:].rstrip('/')
        return fmt_url


    def fetch_articles(self, bias, source_list):
        source_list = self.fetch_sources(bias)
        '''
        if bias < 0:
            articles = self.left_articles
        else:
            articles = self.right_articles

        articles.sort(key = lambda x: arrow.get(x['pubDate']), reverse=True)
        for article in articles:
            article['date'] = arrow.get(article['pubDate']).humanize()

        return articles
        '''
        articles = []
        for source in source_list:
            url = self.format_url(source[1])
            response = self.datanews.headlines(source=url,size=25,sortBy='date')
            hits = response['hits']
            for hit in hits:
                hit['source'] = source
                hit['date'] = arrow.get(hit['pubDate']).humanize()
            articles.extend(hits)

        articles.sort(key = lambda x: arrow.get(x['pubDate']), reverse=True)
        '''
        out_fname = f'{bias}_results.json'
        out_file = open(out_fname, 'w')
        json.dump(articles, out_file)
        out_file.close()
        return articles
        '''

        return articles
        #return (source_list, self.articles)
