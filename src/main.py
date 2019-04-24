import urllib3 as urllib
import xmltodict
import csv

from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_document(doc):
    stopset = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    tokens = wordpunct_tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 2]
    final = [stemmer.stem(word) for word in clean]
    return final


class NYT:
    def __init__(self):
        self.articles = [] # initialize list containing tuples: article corpus - label

    def retrieve(self, nytimes_url, label):
        # code dependent on the nytimes structure of RSS feed
        http = urllib.PoolManager()
        r = http.request('GET', nytimes_url)

        data = xmltodict.parse(r.data)
        data = data["rss"]
        data = data["channel"]
        data = data["item"]

        for key in data:
            article = key
            title, descr, extra_descr = "", "", ""
            if "title" in article and article["title"] is not None:
                title = article["title"] + ". "
            if "media:description" in article and article["media:description"] is not None:
                descr = article["media:description"]
            if "description" in article and article["description"] is not None:
                extra_descr = article["description"]

            corpus = str(title) + str(descr) + str(extra_descr)
            self.articles.append(tuple((corpus, label)))

    def toCSV(self, filename):
        with open(filename, 'w') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['corpus', 'category'])
            csv_out.writerows(self.articles)



nyt = NYT()

nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml', 'Politics')
nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Business.xml', 'Business')
nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml', 'Tech')
nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Science.xml', 'Science')
nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Health.xml', 'Health')
nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Sports.xml', 'Sports')
nyt.retrieve('http://rss.nytimes.com/services/xml/rss/nyt/Arts.xml', 'Arts')


for corpus,label in nyt.articles:
    print("\""+corpus+"\"", label)

#nyt.toCSV("nyt20190423.csv")


