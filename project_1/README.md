# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring climate data of Singapore

Prepared by Timothy Chan, 17 Feb 2023
<br>
<br>
### Overview

This project applies Python programmming for Exploratory Data Analysis (EDA) and Data Visualisation, as well as basic statistics to analyse Singapore rainfall to a data science problem. 

---

### Problem Statement

Food delivery is affected by rainy weather in Singapore. Rain, especially heavy rain, may affect food deliveries in terms of surge in orders, less delivery riders and delays in deliveries. This project aims to analyse the weather patterns in Singapore to identify what strategies food delivery companies can adopt to better manage the rainy weather.

---

### Datasets

Datasets provided corresponding to rainfall information are: 
* [`rainfall_monthly_highest_daily_total.csv`](./data/rainfall_monthly_highest_daily_total.csv): The highest daily total rainfall for the month recorded in millimeters(mm) from 1982 to 2022.
* [`rainfall_monthly_number_of_rain_days.csv`](./data/rainfall_monthly_number_of_rain_days.csv): Monthly number of rain days from 1982 to 2022. A day is considered to have “rained” if the total rainfall for that day is 0.2mm or more.
* [`rainfall_monthly_total.csv`](./data/rainfall_monthly_total.csv): Monthly total rain recorded in millimeters(mm) from 1982 to 2022 <br>
Rainfall information are collected at Changi Climate Station, Singapore. Files are extracted from [data.gov.sg](https://data.gov.sg/).

Additionally, the following datasets are used:
* [`population_by_planning_area_2022.csv`](./data/population_by_planning_area_2022.csv): Population by planning area based on the Urban Redevelopment Authority (URA) Master Plan 2019. Relevant information is the Singapore Residents population by planning area as at June 2022. Extracted from [Singstat](https://www.singstat.gov.sg/find-data/search-by-theme/population/geographic-distribution/latest-data) at this [link](https://www.singstat.gov.sg/-/media/files/find_data/population/statistical_tables/respopagesexfa2022.ashx)
* [`historical daily records of rainfall`](./data/additional_rainfall_data): Relevant information are daily total rainfall, highest rainfall over 30min, 60min and 120 min, all recorded in millimeters(mm). Records from 6 different stations in different areas of Singapore for 2021 and 2022 were extracted from [Meteorological Service Singapore](http://www.weather.gov.sg/climate-historical-daily/)

All links above and within are functioning as of Feb 2023. All datasets are included in the [`data`](./data/) folder.
<br>
<br>
#### Data Dictionary of cleaned data

|Feature|Type|Dataset|Description|
|:---|:---|:---|:---|
|yyyy_mm|string|data_2013_2022|Year and month of rainfall information|
|maximum_rainfall_in_a_day|float|data_2013_2022|Highest daily total rainfall for the month recorded in millimeters(mm) from 2013 to 2022|
|no_of_rainy_days|integer|data_2013_2022|Monthly number of rain days from 2013 to 2022. A day is considered to have “rained” if the total rainfall for that day is 0.2mm or more.|
|total_rainfall|float|data_2013_2022|Monthly total rain recorded in millimeters(mm) from 2013 to 2022|
|year|integer|data_2013_2022|Year of rainfall information|
|month|integer|data_2013_2022|Month of rainfall information|
|station|string|stations_daily_2021_2022|Station and area of rainfall information|
|year|integer|stations_daily_2021_2022|Year of rainfall information|
|month|integer|stations_daily_2021_2022|Month of rainfall information|
|day|integer|stations_daily_2021_2022|Day of the month of rainfall information|
|daily_total_rainfall|float|stations_daily_2021_2022|Daily total rain recorded in millimeters(mm) from 2021 to 2022|
|highest_30min_rainfall|float|stations_daily_2021_2022|Highest rainfall over 30 minutes collected for the day from 2021 to 2022|
|highest_60min_rainfall|float|stations_daily_2021_2022|Highest rainfall over 60 minutes collected for the day from 2021 to 2022|
|highest_120min_rainfall|float|stations_daily_2021_2022|Highest rainfall over 120 minutes collected for the day from 2021 to 2022|
|days_of_heavy_rain|integer|stations_daily_2021_2022|Days with heavy rain from 2021 to 2022. Days with heavy rain = 1 and days with no heavy rain = 0. A day is considered to have heavy rain when there is more than 3.8mm of rain over 30 minutes for that day.|
|planning_area|string|population_by_planning_area|Selected population area based on the Urban Redevelopment Authority (URA) Master Plan 2019|
|population|integer|population_by_planning_area|Population of residents as of June 2022|

---

### Submissions

Technical reports submitted: 
* [`project_1.ipynb`](./project_1.ipynb): Detailed exploratory data analysis and findings.
* [`project_1_slides.pdf`](./project_1_slides.pdf): Presentation slides.

---

### Summary of findings

1. On average, it rained an average of about 14 days a month (about 50% of the month). On average, there was heavy rain for 29% of days in a year.
2. As 2022 had higher than average rain volume, we might expect the same for 2023.
3. Singapore has highest rainfall volume in the months of October to January.
4. However, the months with higher than average number of days with heavy rain are more spread out across the year.
5. There are slightly more days of heavy rain in the North, West and North-East compared to the South and East (15 more days or 4% more days in a year).

---

### Recommendations

Singapore has high rainfall and just like recent years they might need to expect 2023 to have higher than average rain volume, so food delivery companies should definitely consider rainfall when planning their delivery operations, marketing, pricing.

As higher rainfall volume is expected in October to January, there is likely to be surges in food orders during this period. These companies could hire more delivery riders by increasing recruitment efforts for short-term rider or having better incentives to attract more riders to meet the demand during this period. At the same time, they may not need to have as much marketing efforts to attract more food orders during this period. Budget resources could be allocated from marketing promotions to recruitment or delivery completion incentives.

While these food delivery companies can prepare for the rain in October to January, there are also many other months with heavy rain throughout the year. As such, it may not be enough to focus on just the year-end period. More sensitive collection of information or detailed algorithms to identify real-time or expected rain durations and intensity may be necessary. These may help decide whether there should be peak charges to balance order demand and supply of riders, or whether they should set longer expected delivery timings when it rains.

There are also residential areas in Singapore which experiences slightly higher number of days with heavy rainfall than others. Delivery companies can take this into consideration when planning their food delivery operations.

---

### Limitations

Public data on food delivery is unavailable, to compare against rainfall data and make detailed recommendations e.g. number of additional riders needed.

---

### References
*For datasets*
1. https://data.gov.sg/
2. https://www.singstat.gov.sg/
3. http://www.weather.gov.sg/

*For research*
1. https://glossary.ametsoc.org/wiki/Rain
2. http://www.weather.gov.sg/climate-climate-of-singapore/
3. https://www.nea.gov.sg/media/news/news/index/2021-is-singapore-s-second-wettest-year-since-1980
4. https://www.straitstimes.com/singapore/wet-and-windy-start-to-the-new-year-continues-into-saturday
5. https://www.straitstimes.com/asia/se-asia/more-rainy-days-ahead-in-singapore-as-two-weather-phenomena-set-to-bring-grey-skies
6. https://www.todayonline.com/singapore/perks-and-perils-being-food-delivery-rider
7. https://www.straitstimes.com/singapore/heavy-rain-disrupts-chinese-new-year-celebrations
