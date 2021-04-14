import csv
from newspaper import Article
import time
from gnews import *

# given a R / L bias -> first get list of R / L sources
# with list of sources -> get lists of articles for R / L each


l_bias = -25
r_bias = 30

googlenews = GoogleNews(lang='en')
googlenews.set_period('1h')

def get_sources(source_list, bias, radius):
    idx = int(bias * len(source_list))
    results = [source_list[idx]]
    cur_radius = 1
    while cur_radius <= radius:
        if idx - cur_radius >= 0:
            results.append(source_list[idx-cur_radius])
        if idx + cur_radius < len(source_list):
            results.append(source_list[idx+cur_radius])
        cur_radius += 1
    return results


def get_articles(sources):
    articles = []
    for source in sources:
        search_term = 'site:' + source[1]
        googlenews.search(search_term)
        results = googlenews.results()
        articles.extend(results)
        '''
        for result in results:
            articles.append(result)
            article = Article(result['link'])
            article.download()
            article.parse()
            result['img'] = article.top_image
            articles.append(result)
        '''
        googlenews.clear()
    return articles

if __name__ == "__main__":
# parse the CSV and store in memory

    csvfile = open('output.csv', 'r')
    reader = csv.reader(csvfile)

    sources = []
    for row in reader:
        sources.append((row[0], row[1], float(row[3])))

    r_sources = [s for s in sources if s[2] > 0.0]
    l_sources = [s for s in sources if s[2] < 0.0]

    l_sources.sort(key=lambda tup: abs(tup[2]))
    r_sources.sort(key=lambda tup: tup[2])

    test_l = get_sources(l_sources, 0.9, 1)
    test_r = get_sources(r_sources, 0.7, 1)

#    print(get_articles(test_l))

    start = time.time()
    right_articles = get_articles(test_r)
    left_articles = get_articles(test_l)
    end = time.time()
    print("elapsed: ", end - start)


 #   l_map = [[] for x in range(int(l_sources[0][2]))]


    csvfile.close()
    '''
    url = "amgreatness.com"
    googlenews.get_news(url)
    results = googlenews.get_texts()
    print(results)

    '''
