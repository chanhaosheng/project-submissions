# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2 - Singapore Housing Data and Kaggle Challenge

Prepared by Timothy Chan, 3 Mar 2023
<br>
<br>
### Overview

This project applies Exploratory Data Analysis (EDA) and Basic Regression Modelling to predict the price of houses on sale based on Singapore Housing Dataset. Models to be applied using Scikit-Learn are: Linear Regression, Lasso Regularisation and Ridge Regularisation.

---

### Problem Statement

Resale flat transactions are substantial: they accounted for [60.5% of all sale transactions in 3rd Quarter 2022](https://www.ura.gov.sg/Corporate/Media-Room/Media-Releases/pr22-38).

A real estate agent company in Singapore would like to know how to advise clients on the appropriate prices to list their flats for resale. They require a reproducable model to predict Housing & Development Board (HDB) resale prices based on available information about the flat, as well as to understand the key factors affecting pricing of resale flats.

### Evaluation
Models will be evaluated using root mean square error (RMSE) score while taking into consideration the number of features used.

---

### Datasets

Datasets provided: 
* [`train.csv`](./datasets/train.csv): Training data for modelling. Resale flat transactions between Mar 2012 and Apr 2021.
* [`test.csv`](./dataset/test.csv): Test data for the model. Resale flat transactions between Mar 2012 and Apr 2021. Target variable (resale_price) is removed.

<br>

#### Data dictionary of cleaned training and testing files before performing one-hot encoding.

|Features|Type|Dataset|Description|
|:---|:---|:---|:---|
|id|float|flats_test_cleaned.csv||
|resale_price|float|flats_cleaned.csv|Property's sale price in Singapore dollars. Our target variable to predict|
|floor_area_sqft|float|both|Floor area of the resale flat unit in square feet|
|price_per_sqft|float|both|Price in Singapore dollars for each square feet of floor area. Not to use for model|
|street_name|string|both|Street name where the resale flat resides. For reference only|
|address|string|both|Address where the resale flat resides. For reference only|
|latitude|float|both|Latitude based on postal code. For reference only|
|longitude|float|both|Longtitude based on postal code. For reference only|
|flat_type|string|both|Type of the resale flat unit, e.g. 3 ROOM|
|flat_model|string|both|HDB model of the resale flat, e.g. Multi Generation|
|planning_area|string|both|Government planning area that the flat is located|
|postal_sector|integer|both|first two digits of six digit postal code|
|max_floor_lvl|integer|both|Highest floor of the resale flat|
|mid_storey|integer|both|Estimated floor level of unit based on median value of storey range|
|hdb_age|integer|both|Number of years from lease commencement date to year of data (2021)|
|mrt_interchange|integer|both|boolean value if the nearest MRT station is also a train interchange|
|bus_interchange|integer|both|boolean value if the nearest MRT station is a bus interchange station|
|mrt_nearest_distance|float|both|distance in metres to the nearest MRT station|
|hawker_nearest_distance|float|both|distance in metres to the nearest hawker centre|
|distance_to_cityhall|float|both|distance in metres to the CBD|
|hawker_within_2km_imp|float|both|number of hawker centres within 2 kilometres (missing values imputed)|
|mall_within_2km_imp|float|both|number of malls within 2 kilometres (missing values imputed)|
|total_dwelling_units|integer|both|total number of residential dwelling units in the resale flat|
|commercial|integer|both|if resale flat has commercial units in the same block|
|flat_type_tgt|float|both|target encoding of mean price per sqft of each category of flat type|
|flat_model_tgt|float|both|target encoding of mean price per sqft of each category of flat model|
|planning_area_tgt|float|both|target encoding of mean price per sqft of each category of planning area|
|postal_sector_tgt|float|both|target encoding of mean price per sqft of each category of postal sector|

---

### Submissions

Technical reports submitted: 
* [`project_2_part1.ipynb`](./project_2_part1.ipynb): Data Cleaning and Exploratory Data Analysis (EDA). This is done individually.
* [`project_2_part2.ipynb`](./project_2_part2.ipynb): Preprocessing, Modelling and Recommendations. This is done individually.
* [`project_2_slides.pdf`](./project_2_slides.pdf): Presentation slides. This is done as a group using another team-member's model. Content is different.

---

### Summary

A Lasso Model on 30 features was chosen, with a root mean squared error (RMSE) of about 53,000. There is little overfitting.

Features can be categoried as:
1. Floor area. The larger the area, the higher the price. This is the largest factor by far.
2. HDB age. The longer the lease aged, the lower the price. This is the second largest factor.
3. Convenience (5 features: distance to CBD, MRT, Hawker; Number of Hawkers; Bus interchange at nearest MRT)
4. Location (14 selected planning areas). Marine Parade, Bishan and Queenstown are some locations which command higher prices in this model. Woodlands and Sembawang are some locations which command lower prices.
5. Flat type and models (6 selected type/models, such as DBSS or Terrace which are more premium and more rare).
6. Number of dwelling units. Denser flats may have more noise and are less attractive.

---

### Recommendations

The prediction model for the real estate agent company is able to predict HDB resale prices with an RMSE of 53,000. 

Generally, buyers look most at size, age, convenience and location when purchasing the flats, as seen in the model. They may also consider flat types/models and how dense the flat is. The real estate agent company can consider focusing on these factors when selling the flat to their potential customers.

---

### Possible improvements

- larger dataset to reduce error and improve score
- updated dataset to train the data
- more indicative features e.g. specific characteristics of each location; flat condition
- more advanced models rather than linear regression
- improve target encoding used to avoid overfitting

---

### References
*Research*
1. https://www.propertyguru.com.sg/property-guides/hdb-valuation-sales-12882
2. https://www.teoalida.com/singapore/lease/
3. https://www.singsaver.com.sg/blog/average-cost-of-home-renovations-singapore
4. https://www.ura.gov.sg/Corporate/Media-Room/Media-Releases/pr22-38

