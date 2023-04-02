# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4 - West Nile Virus Prediction (Kaggle)

Prepared by: Kho Guan Guo, Soh Sze Ron, Timothy Chan, 3 Apr 2023
<br>
<br>
### Overview
<br>

**Background**

In 2002, the first human cases of West Nile virus were reported in Chicago. By 2004 the City of Chicago and the Chicago Department of Public Health (CDPH) had established a comprehensive surveillance and control program that is still in effect today.

Every week from late spring through the fall, mosquitos in traps across the city are tested for the virus. The results of these tests influence when and where the city will spray airborne pesticides to control adult mosquito populations.

West Nile virus, is typically spread by mosquitoes. In about 80% of infections people have few or no symptoms. About 20% of people develop a fever, headache, vomiting, or a rash. In less than 1% of people, encephalitis or meningitis occurs, with associated neck stiffness, confusion, or seizures. Recovery may take weeks to months. The risk of death among those in whom the nervous system is affected is about 10 percent. People can reduce their risk of WNV by using insect repellent and wearing long-sleeved shirts and long pants to prevent mosquito bites.

The cost of treatment for severe symtoms developed from WNV can be staggeringly high. Preventative measures like spraying of pesticides, can also be costly and potentially harmful to the environment. It is thus essential to manage the spread of WNV efficiently and effectively.
<br><br>
**Problem Statement**

We are employees of the Disease And Treatment Agency, division of Societal Cures In Epidemiology and New Creative Engineering (DATA-SCIENCE). Due to the recent epidemic of West Nile Virus in the Windy City, we've had the Department of Public Health set up a surveillance and control system.

Our role is to derive an effective plan to deploy pesticides throughout the city:

- create a model to predict the presence of WNV throughout various locations in the city of Chicago
- do a cost benefit analysis to weigh cost of spraying pesticides against potential benefits

The model and the analysis should serve to help the city better manage resources when dealing with WNV.
<br><br>
**Evaluation**

This is a classification problem.

Models were evaluated by AUC score on Kaggle. After optimizing AUC score, we will also ensure validation recall score is above 0.70 and adjust if necessary.

---

### Datasets

Datasets are provided on Kaggle.

Datasets: 
* [`train.csv`](./data/train.csv)
* [`test.csv`](./data/test.csv)
* [`spray.csv`](./data/spray.csv)
* [`weather.csv`](./data/weather.csv)

<br>

#### Data dictionary of selected features only

|Features|Type|Description|
|:---|:---|:---|
|wnv_present|boolean|1 if West Nile Virus was present in these mosquitos when tested; 0 if it is not|
|wet_bulb|int|average wet bulb temperature in degrees fahrenheit|
|result_speed|float|vector sum of wind speed and direction in mph|
|minutes_between|int|daylight duration between sunrise and sunset in minutes|
|species_culex_xx|boolean|1 if it is that species of mosquitos; 0 if it is not|
|cluster_label_xx|boolean|1 if it is located in that cluster; 0 if it is not|

---

### Submissions

Technical reports submitted: 
* [`project_4_part1.ipynb`](./project_4_part1.ipynb): Overview and Data Cleaning
* [`project_4_part2.ipynb`](./project_4_part2.ipynb): EDA
* [`project_4_part3.ipynb`](./project_4_part3.ipynb): Feature Selection and Modelling
* [`project_4_part4.ipynb`](./project_4_part4.ipynb): Cost-Benefit Analysis and Recommendations

---

### Modelling

**Summary of results**

|Model|Classifier|AUC (CV)|AUC (Train)|AUC (Val)|AUC (Kaggle)|Recall (Val)|Pros|Cons|
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|1|Logistic Regression|0.786|0.798|0.791|0.656|0.781|fast; easy to interpret|may not capture complex/non-lineaer relationship|
|2|Logistic Regression (less features)|0.760|0.768|0.748|0.582|0.772|fast; easy to interpret|may not capture complex/non-lineaer relationship|
|3|Multinomial Naive Bayes|0.705|0.716|0.708|N/A|0.737|fast and simple|may not capture complex/non-linear relationship|
|5|Random Forest|0.820|0.885|0.838|0.609|0.702|robust to noise; can capture complex/non-linear relationship|slower|
|6|Random Forest (less features)|0.821|0.867|0.822|0.680|0.693|robust to noise; can capture complex/non-linear relationship|slower|
|7|XGBoost|0.832|0.882|0.844|0.579|0.544|robust to noise; can capture complex/non-linear relationship|slower|
|8|XGBoost|0.825|0.855|0.832|0.600|0.693|robust to noise; can capture complex/non-linear relationship|slower|
|9|**Random Forest (less Features) finetuned**|0.823|0.859|0.822|**0.701**|0.746|robust to noise; can capture complex/non-linear relationship|slower|

Random Forest had the least amount of overfitting when tested using the Kaggle dataset. It had a test AUC score of 0.701. It also has a reasonable recall score of 0.772.

Only a few features were used to avoid overfitting:
- sunlight duration
- week number
- wet bulb temperature
- wind resultant speed
- 3 species categories

**Possible improvements**

It was quite challenging to get a good score. This could be because of how the Kaggle datasets were designed: train (2007, 2009, 2011, 2013) and test data (2008, 2010, 2012, 2014) were split in alternate years. We have to use data from some years to predict results for other years. While not exactly a time-series problem, this makes it more unpredictable as there could be other factors such as time element or year specific elements which could not be identified and trained (without looking at the test data).

Even though there is very little overfitting when doing train-test split and validating, it was heavily overfitted on the test data. In hindsight, we could further explore techniques in designing validation to overcome this issue. For example, we could do train-test split by years, and perform training and validation on different years. This might make the model more robust to year sensitive elements.

---

### Cost Benefit Analysis

We used a base scenario as a benchmark and analysed if having a targeted coverage (spraying only those areas predicted to have WNV present) and/or spraying only in months with peak number of cases would have a lower breakeven point and higher net benefit.

|  | Coverage | Total Costs (\$) | Total Benefits (\$) | Breakeven Cases |  Net Benefit (\$) |
|---|---:|---:|---:|---:|---:|
| Base Scenario | 100% | 2.558m | 2.194m | 106 | -364k |
| 28% Spray Coverage | 28% | 0.713m | 1.636m | 40 | 923k |
| Spray in Peak Months only | 100% | 1.705m | 1.865m | 83 | 160k |
| Monthly Basis | 100% | 0.640m | 0.549m | 106 | -91k |
| Fortnightly Basis | 100% | 1.279m | 1.097m | 106 | -182k |
| **28% Coverage + Peak Months** | 28% | **476k** | 1.39m | **31** | **914k** |

---

### Recommendations

As our hybrid approach has a breakeven point of only 31 cases, and the lowest spend on costs, we will proceed to choose this approach. This analysis has shown that a combined approach of spraying in peak months with a targeted 28% spray in high-risk areas has proved more effective and cost-efficient than simply spraying without proper planning.

Other alternatives:

- Subsidising costs of pesticide
- Agricultural Drones
- Explore possibility of lab-grown mosquitoes
---

### Conclusion

From our analysis conducted, we observe that the key factors that significantly impact the presence and spread of the West Nile virus are: daylight duration ('minutes_between'), period of the year ('week_number'), wet bulb temperature, wind speed and mosquito species.  

The analysis also highlights the importance of targeted spraying in high-risk areas during peak months as an effective approach to controlling the spread of the virus. It is recommended to use a combination of these approaches to maximize the benefits and cost-efficiency of the intervention.

This targeted approach relies on having a a good predictive model. Good information on peak months will also allow better optimisation of spraying cost-to-benefit. Our current best model (Random Forest) is respectable with AUC and Recall score both more than 0.70.
<br><br>
**Future improvements** <br>
In order to improve the AUC score further, we might need to explore techniques in designing validation to overcome these issues and make the models more robust. We could also use more data to train the model.

Additionally, we could also consider the long-term effects of West Nile Virus. For roughly 1 in every 150 infections, manifests into a severe neurological disease called West Nile Neuroinvasive Disease (WNND). For non-neuroinvasive WNV cases, the percentage of deaths is only 0.5%. However for WNND, the % of deaths is much higher at 9%. Including this in our cost-benefit analysis might get a more realistic assessment but will also make the analysis more complex.

---

### References

- [www.beyondpesticides.org/resources/mosquitos-and-insect-borne-diseases/documents/the-truth-about-mosquitoes,-pesticides-and-west-nile-virus](www.beyondpesticides.org/resources/mosquitos-and-insect-borne-diseases/documents/the-truth-about-mosquitoes,-pesticides-and-west-nile-virus)
- [https://www.orkin.com/pests/mosquitoes/when-are-mosquitoes-most-active](https://www.orkin.com/pests/mosquitoes/when-are-mosquitoes-most-active)
- [https://www.mosquitomagnet.com/advice/mosquito-info/biting-insect-library/culex-pipiens-mosquito](https://www.mosquitomagnet.com/advice/mosquito-info/biting-insect-library/culex-pipiens-mosquito)
- [www.chicago.gov/content/dam/city/depts/cdph/Mosquito-Borne-Diseases/Zenivex.pdf](www.chicago.gov/content/dam/city/depts/cdph/Mosquito-Borne-Diseases/Zenivex.pdf)
- [bidcondocs.delaware.gov/NAT/NAT_19123-INSECTICIDE_An.pdf](bidcondocs.delaware.gov/NAT/NAT_19123-INSECTICIDE_An.pdf)
- [https://www.cmmcp.org/pesticide-information/pages/zenivex-e4-etofenprox](https://www.cmmcp.org/pesticide-information/pages/zenivex-e4-etofenprox)
- [www.astmh.org/CMSPages/GetFile.aspx?guid=823fde2b-6fa4-4e07-ae52-9dc10f1d5e54](www.astmh.org/CMSPages/GetFile.aspx?guid=823fde2b-6fa4-4e07-ae52-9dc10f1d5e54)
- [https://www.npr.org/sections/health-shots/2014/02/11/275262857/the-high-cost-of-treating-people-hospitalized-with-west-nile-virus](https://www.npr.org/sections/health-shots/2014/02/11/275262857/the-high-cost-of-treating-people-hospitalized-with-west-nile-virus#:~:text=The%20U.S%20recorded%20its%20first,of%20Tropical%20Medicine%20and%20Hygiene)
- [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241786/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7241786/#:~:text=There%20were%201%2C371%20total%20human,(Cook%20and%20DuPage%20Counties))
- [https://www.cdc.gov/westnile/statsmaps/cumMapsData.html#one](https://www.cdc.gov/westnile/statsmaps/cumMapsData.html#one)
- [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322011/#R5](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3322011/#R5)
- [https://www.todayonline.com/singapore/nea-opens-new-facility-breed-5-million-mosquitoes-week-combat-dengue](https://www.todayonline.com/singapore/nea-opens-new-facility-breed-5-million-mosquitoes-week-combat-dengue)