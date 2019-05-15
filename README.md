# Profile Based Retrieval System
The aim of the project is to investigate methods based in the space vector model to deliver small text snippets to different users depending on their profile. 
For instance, let us suppose that we have 4 different users: the first one being interested in politics and soccer, the second in music and films, the third in cars and politics and the fourth in soccer alone. An incoming document targeted at politics should be delivered to users 1 and 3, while a document on soccer should be delivered to users 1 and 4. 
After developing a classification model for news articles, two possible use cases were proposed:
1. Profile-Driven Search Engine for News Articles
2. Profile-Based Newsletter  

Below you will find a short overview. However, you can find all the needed informations in the report.

## Profile-Driven Search Engine for News Articles
Personalized search refers to web search experiences that are tailored specifically to an individual’s interests by incorporating information about the individual beyond specific query provided. In this case, for each individual we know which are the categories to which it is interested to. One example is Google. Google often shows the ability to personalize searches in its use of Google News. They implement this feature in its news to show everyone a few similar articles that can be interesting. 

## Profile-Based Newsletter  
In this era of information explosion, providing the right information to the right person within reasonable time duration is a very important goal for today’s information retrieval (IR) systems. In this use case, a user wants to retrieve all the news available on the web, that are related to his interests. The system retrieves a set of news articles, classify them and finally distributes the news to the most appropriate users. This behaves like a newsletter, but with the integration of an automatic system to estimate the probability of relevance of that article for that user.

## Data
News articles were retrieved in English language, to be able to use the most advanced toolkits avail-
able in the NLP research field. Different data sources were exploited: 
- [New York Times RSS feeds](https://www.nytimes.com/)
- [BBC News RSS feeds](https://www.bbc.com/news)
- [The Guardian RSS feeds](https://www.theguardian.com/us)
- [Kaggle - News Category Dataset - Misra 2018](https://www.kaggle.com/rmisra/news-category-dataset)

User profiles instead, were randomly generated. There is no need to use real user data in this project.

