# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3 - Web APIs & NLP on Internet and Alcohol Addiction Subreddits

Prepared by Timothy Chan, 17 Mar 2023
<br>
<br>
### Overview

This project applies Web Scraping, Data Cleaning, Exploratory Data Analysis (EDA) and Basic Natural Language Processing and Classification Modelling to train a classifier on two subreddits. 

Pushshift API was used for Web Scraping. Natural Language Toolkit (NLTK) and Scikit-Learn (sklearn) were used for pre-processing of text. Models applied were Logistic Regression, Multinomial Naive Bayes, Random Forest and Gradient Boosting. Vectorizers used were Count Vectorizer and TF-IDF Vectorizer.

---

### Problem Statement

Around [8% of the global population is addicted to the internet](https://techjury.net/blog/technology-addiction-statistics/), which can lead to negative consequences such as social isolation and health problems. Furthermore excessive internet use has not been recognized as a disorder by the World Health Organization, the Diagnostic and Statistical Manual of Mental Disorders (DSM-5) or the International Classification of Diseases (ICD-11).

Meanwhile, alcohol addiction has limited treatment options and can have a significant impact on individuals, families, and communities. [Over 70% of individuals with alcohol abuse will relapse at some point](https://www.therecoveryvillage.com/alcohol-abuse/alcohol-relapse-statistics/), and stigma may prevent them from seeking help.

A non-profit organization aims to develop a chatbot to provide users with personal advice and resources on internet and alcohol addiction based on the addiction category detected from their question. To facilitate this, they require a machine learning model that can differentiate between the two addictions based on users' questions. My role is to provide the machine learning model.

### Evaluation
This is a natural language processing (NLP) binary classification problem.

Models were evaluated by accuracy score.

---

### Datasets

Pulled posts from `r/nosurf` and `r/stopdrinking` as proxy of internet and alcohol addiction using `Postshift API`. 1,000 posts before UTC 2023-03-07 00:00:00 for both subreddits were scraped.

Subreddit description of `r/nosurf`:
NoSurf is a community of people who are focused on becoming more productive and wasting less time mindlessly surfing the internet.

Subreddit description of `r/stopdrinking`:
This subreddit is a place to motivate each other to control or stop drinking. We welcome anyone who wishes to join in by asking for advice, sharing our experiences and stories, or just encouraging someone who is trying to quit or cut down. Please post only when sober; you're welcome to read in the meanwhile.

Datasets saved: 
* [`data_nosurf.csv`](./datasets/data_nosurf.csv)
* [`data_stopdrinking.csv`](./dataset/data_stopdrinking.csv)

<br>

#### Data dictionary of cleaned data

|Features|Type|Description|
|:---|:---|:---|
|subreddit|integer|subreddit in which data is extracted from|
|text|string|combination of title and subject of each subreddit post|
|text_cleaned|string|cleaned and preprocessed text|
---

### Submissions

Technical reports submitted: 
* [`project_3_part1.ipynb`](./project_3_part1.ipynb): Data Collection
* [`project_3_part2.ipynb`](./project_3_part2.ipynb): Data Cleaning, Preprocessing, EDA, Modelling and Recommendations
* [`project_3_slides.pdf`](./project_3_slides.pdf): Presentation slides

---

### Summary

|Model|Classifier|Vectorizer|Accuracy (CV)|Accuracy (Train)|Accuracy (Test)|False Positive|False Negative|
|:---|:---|:---|:---|:---|:---|:---|:---|
|1|**Multinomial NB**|**Count Vectorizer**|0.957|0.963|**0.944**|11|17|
|2|Multinomial NB|TF-IDF Vectorizer|0.956|0.976|0.936|15|17|
|3|Logistic Regression|Count Vectorizer|0.938|0.981|0.934|18|15|
|4|Logistic Regression|TF-IDF Vectorizer|0.949|0.987|0.932|18|16|
|5|Random Forest|Count Vectorizer|0.943|0.959|0.924|7|31|
|6|Random Forest|TF-IDF Vectorizer|0.941|0.965|0.940|18|12|
|7|Gradient Boosting|Count Vectorizer|0.933|0.977|0.920|28|12|
|8|Gradient Boosting|TF-IDF Vectorizer|0.919|0.997|0.918|29|12|

Count Vectorizer with Multinomial Naive Bayes (Model 1) has the best accuracy. This model was chosen.

---

### Recommendations

The selected model, Count Vectorizer with Multinomial Naive Bayes, has high accuracy of 0.944. Besides one or two cases, those False results are mostly due to input issues and not the model issue. The accuracy should improve even further if it includes the obvious phrases which were excluded for this project. As such the model is well suited for the chatbot.

In addition, although higher accuracy means better user experience, it is not critical (and possible) for the chatbot to be fully accurate. The chatbot should be designed to consider such cases. For example, misclassification can be rectified through clarification by chatbot user that he/she has been assigned wrongly. The chatbot can then route the user to the correct set of advice and recommendations.

Preprocessing was mostly automated. Most stopwords were removed using available stopword sets and there was minimal manual removal of stopwords. This means that there should be minimal maintenance efforts (e.g. modifying/adding new stopwords) after implementation.

The top coefficients of the selected model highlights common phrases. These relate mostly to medium, actions and ways to curb the habits among others. It also highlights some phrases we may not expect or familiar with, but are commonly used in these topics (e.g. 'iwndwyt', 'NA').

---

### Possible improvements

- More data to improve score further
- Multiple sources besides Reddit for better reflection of words to be trained
- Finetuning of hyperparameters, especially for ensemble models to improve performance and/or reduce overfitting. However, this requires more time or resources
- Extend to other types of addictions or more targeted advice based on needs (e.g. for community or emotional support, or to get tips etc)

---

### References
*Subreddits*
1. https://www.reddit.com/r/nosurf/
2. https://www.reddit.com/r/stopdrinking/

*Research*
1. https://www.therecoveryvillage.com/alcohol-abuse/alcohol-relapse-statistics/
2. https://techjury.net/blog/technology-addiction-statistics/

