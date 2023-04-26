# OTTO Multi-Objective Recommender System

Prepared by: Timothy Chan, 27 Apr 2023
<br>
<br>
### Overview
<br>

**Background**

Good recommendations on online shopping platforms can enhance buyer experience; allowing them to select more relevant items that they would click and buy. It would also increase engagement and spending for the ecommerce platform.

Otto (https://www.otto.de/), an ecommerce platform organised a Kaggle Competition for participants to explore how to build a single entry predicting click-through, add-to-cart, and conversion rates based on previous same-session events, and recommend relevant items based on real-time behavior.
<br><br>
**Problem Statement**

My role is to use implicit information to build and deploy a model to predict the next 20 clicks, carts and orders for each user. By building an effective model to predict relevant items, user experience and ecommerce platform performance will be better.
<br><br>
**Evaluation**

Scores are evaluated on `Recall@20` for each action type, and the three recall values are weight-averaged:

    Score = (0.10 ⋅ Rclicks) + (0.30 ⋅ Rcarts) + (0.60 ⋅ Rorders)

where

    R = TP / P
TP is the number of correctly predicted items and P is lower of 20 or the number of ground truth items. 

Recall@k is the proportion of relevant items found in the top-k recommendations. Recall@k is a suitable metric as it measures the platform's ability to recommend all the relevant items that the user might be interested in.

---

### Datasets

Datasets are provided on Kaggle in jsonl format. As my machine is unable to read jsonl, I used a compressed version in parquet form shared on [Kaggle](https://www.kaggle.com/datasets/radek1/otto-full-optimized-memory-footprint). 

Data are is between 2022-08-01 and 2022-08-28 for train and between 2022-08-29 and 2022-09-04 for test.

Datasets:
* `train.parquet`
* `test.parquet`

<br>

#### Data dictionary

|Features|Type|Description|
|:---|:---|:---|
|session|integer|the unique session id. Each session represents all user activites during the timeframe|
|aid|integer|the article id (product code) of the associated event|
|ts|integer|the Unix timestamp of the event.|
|type|integer|the event type, i.e., whether a product was clicked (0), added to the user's cart (1), or ordered (2) during the session|

---

### Submissions

Technical reports submitted under `code` folder: 
* [`1.1_understand_data.ipynb`](./code/1.1_understand_data.ipynb): Understanding and splitting the data
* [`1.2_processing_data.ipynb`](./code/1.2_processing_data.ipynb): Splitting the data
* [`1.3_more_processing_data.ipynb`](./code/1.3_more_processing_data.ipynb): Splitting the data
* [`2.0_eda.ipynb`](./code/ottorec_part2.0_eda.ipynb): EDA
* [`3.0_baseline_model.ipynb`](./code/3.0_baseline_model.ipynb): Baseline model
* [`4.1_rule_based_model_covisitation_matrix.ipynb`](./code/4.1_rule_based_model_covisitation_matrix.ipynb): Rule based approach using covisitation matrix
* [`4.2_rule_based_model_covisitation_matrix_x3.ipynb`](./code/4.2_rule_based_model_covisitation_matrix_x3.ipynb): Rule based approach using 3x covisitation matrix and click / buy differentiation
* [`5.0_validate_intuition.ipynb`](./code/5.0_validate_intuition.ipynb): Fast experiments to validate intuitions
* [`6.1_reranker_prepare_train_candidates.ipynb`](./code/4.2_rule_based_model_covisitation_matrix_x3.ipynb): Prepare train candidates for Reranker
* [`6.2_reranker_prepare_test_candidates.ipynb`](./code/6.2_reranker_prepare_test_candidates.ipynb): Prepare test candidates for Reranker
* [`6.3_reranker_add_features.ipynb`](./code/6.3_reranker_add_features.ipynb): Add features to candidates for Reranker
* [`6.4_reranker_lgbm.ipynb`](./code/6.4_reranker_lgbm.ipynb): Rerank using LGBM Ranker
* [`6.5_reranker_xgb.ipynb`](./code/6.5_reranker_xgb.ipynb): Rerank using XGB Ranker

Deployment codes are submitted under `deploy` folder:
* [`app.py`](./deploy/app.py): Application to run the model
* [`box.png`](./deploy/box.png): Image of box as proxy of item images
* [`demo.gif`](./deploy/demo.gif): Demonstration of app working
* [`model.txt`](./deploy/model.txt): Saved LGBM Ranker model
* [`requirements.txt`](./deploy/requirements.txt): List of libraries with versions
* [`test_deploy.parquet`](./deploy/test_deploy.parquet): Reduced dataset to run the model

Slides:
* [`slides.pdf`](./slides.pdf)

---

### Approach

Rule based models have far less steps and if done correctly, can have good and explanable results. Our approach was to push the Rule-based model as far as we can, before using a boosting reranker (a black box model) to push the score further.

<br>

Key issues and how it was resolved:
- Large dataset: To reduce memory error and runtime, we used parquet format, reduced integer forms, split files in chunks, polars, GPUs and Rapid cuDF. Everything was run on Google Colab.
- Cold start problem: Included covisitation pairs. If there are not enough products viewed/purchased, we will use items that are usually viewed and bought together with those few viewed/purchased by user.
- Multiple objectives: We differentiated ranking methods for clicks and buys (carts/orders), then focused only on Orders for reranker which is more tedious.

<br>

### Modelling

**Summary of results**

|Model|Classifier|Brief Description|Recall@20 Score|Comments|
|:---|:---|:---|:---|:---|
|1|Rule-based|Most recent items for each user|0.46682||
|2|Rule-based|Weighted + Covisitation matrix|0.51218||
|3|**Rule-based**|Weighted + Differentiation + 3x Covisitation matrix|**0.57648**|Requires GPU+Rapids|
|4|LGBM Ranker|Reranked from 30 ranked candidates|0.55088|Used Polars, Orders only|
|5|XGB Ranker|Reranked from 30 ranked candidates|0.45841|Requires GPU+Rapids, Orders only|

Rule-based approach gave the best score, was easiest to understand and had far less steps. As such we recommend using the rule-based ranker (Model 3). <br>

Theoretically, a Ranker should give a higher score. However it failed to do so possibily due to a few reasons:
- not enough candidates (requires more machine resources to increase)
- not enough features (requires much more experimentation to produce)
- overfitting between train and test data (in hindsight, should have done thorough validation)

For deployment, we will explore using LGBM Ranker (Model 4) as the scoring is not far off. As the deployment serves more as a proof of concept, we will also keep all the above features.

**Findings: Key features**
- Recency. Items with recent actions have greater influence on the next item.
- Type. Items in carts (or that were carted) have higher tendency of items being orders.
- Frequency of click/buys.
- Covisitation. If items were clicked/purchased on the same day.

**Other applications**
- New user vouchers to encourage activity, to reduce cold start problem
- Identify bundled deals / recommend complementary items

**Possible improvements (given more time and GPU resources)**
- In hindsight, I could built a better pipeline including validation so that I could experiment and select better candidates/features/hyperparameter for the reranker. However, doing multiple experiments is also resource intensive
- Explore Word2Vec to create more candidates. Based on the idea that words that appear in similar contexts are likely to have similar meanings, we could use Word2Vec to identify similarities found within sequence of items.
- Explore Matrix Factorisation to create more candidates. Matrix Factorization produces a user-to-product matrix of the user's preference of each product. KNN for example could be used to identify and rank the similarity.
- Explore Ensembling. Produce multiple models before aggregating.

---

### Conclusion

Handling a large dataset requires many considerations and also limits the amount of exploration that can be done. This needs to be taken into account when planning the modelling process.

There is much insight that a data with only user/session, item, timestamp and action type can provide to make prediction for recommenders. With additional information such as product categories or user demographics, it can only improve the recommendation even further. 

Rule based approaches might be more practical than boosting rankers, while providing reasonable scores. Boosting rerankers should theoretically improve the scores further, but unfortunately did not do so for my project.

---

### References
Many of the ideas and codes were adopted from the Kaggle public discussions, especially from `Chris Deotte` and `Radek Osmulski`. I've learnt a lot from these sharing.

Links:
- Kaggle competition: https://www.kaggle.com/competitions/otto-recommender-system/
- Rapids: https://rapids.ai/

