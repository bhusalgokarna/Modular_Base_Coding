## Traffic Accident Analysis in Belgium (2019-2023)

### Overview
**This project focuses on analyzing traffic accidents in Belgium over the years 2019 to 2023. The data includes various aspects such as the number and severity of accidents, regional and temporal differences, road types, light conditions, and collision types.**

I have used the Belgium open source website (https://statbel.fgov.be/) to download data. I wanted to do analysis not only for 1 year but for last 5 years to see the traffic accident trend by year in Belgium. As latest data i find 2023, I use data from 2019 to 2023 to do this project.

Data  were saved in different formate(.xlsx and .txt), 1st step to read different formates and files data and save in one csv file to make our data reading process easier.

To do this step i create a read data pipeline because this will make my code widly flexible to read different kind of formates and sources.

**Columns of the merged data-frame:**

['DT_DAY', 'DT_HOUR', 'CD_DAY_OF_WEEK', 'TX_DAY_OF_WEEK_DESCR_FR',
       'TX_DAY_OF_WEEK_DESCR_NL', 'CD_BUILD_UP_AREA',
       'TX_BUILD_UP_AREA_DESCR_NL', 'TX_BUILD_UP_AREA_DESCR_FR',
       'CD_COLL_TYPE', 'TX_COLL_TYPE_DESCR_NL', 'TX_COLL_TYPE_DESCR_FR',
       'CD_LIGHT_COND', 'TX_LIGHT_COND_DESCR_NL', 'TX_LIGHT_COND_DESCR_FR',
       'CD_ROAD_TYPE', 'TX_ROAD_TYPE_DESCR_NL', 'TX_ROAD_TYPE_DESCR_FR',
       'CD_MUNTY_REFNIS', 'TX_MUNTY_DESCR_NL', 'TX_MUNTY_DESCR_FR',
       'CD_DSTR_REFNIS', 'TX_ADM_DSTR_DESCR_NL', 'TX_ADM_DSTR_DESCR_FR',
       'CD_PROV_REFNIS', 'TX_PROV_DESCR_NL', 'TX_PROV_DESCR_FR',
       'CD_RGN_REFNIS', 'TX_RGN_DESCR_NL', 'TX_RGN_DESCR_FR', 'MS_ACCT',
       'MS_ACCT_WITH_DEAD', 'MS_ACCT_WITH_DEAD_30_DAYS',
       'MS_ACCT_WITH_MORY_INJ', 'MS_ACCT_WITH_SERLY_INJ',
       'MS_ACCT_WITH_SLY_INJ']

**35 columns :**
English, Dutch and French. each language has their own columns for same information, we will keep only one from three. and rename the column name to make more readable, understandable by column name.

**176277 rows :**

**Most of column's dtypes is Object.**
Missing values in Buid-up area, coll_type, Light Condition, Road-Type and provincie.

After seeing the original data, we need to follow some cleaning and validating steps. Check src/verkeerOngevallen/models/data_processor.py file to see more details about this process. This step is responsible for data cleaning, validating and data transforming. This design promotes Polymorphism, enabling you to interchange implementations easily.

By segregating these responsibilities, we ensure that changes in one area (e.g., adding a new data source) don't inadvertently impact another area
(e.g., data cleaning logic).

**After cleaning our data, now its time to see and go through clean datafram :**

Data cleaning, validating, transforming is the crusial steps to do data analysis. As we can see above clean_df, data is organized, more readable, validated data to do further analysis.

**Columns : 19**

#### ['Hour', 'DayOfWeek', 'BuiltUpArea', 'CollisionType', 'LightCondition','RoadType', 'Municipality', 'District', 'Province', 'Region','Accident', 'AccidentsWithFatalities', 'AccidentsWithFatalities30Days','AccidentsWithMinorInjuries', 'AccidentsWithSeriousInjuries','AccidentsWithSlightInjuries', 'Year', 'Month', 'Day_of_Month'],


**rows : 176274**

As you can see from above we didn't lose any  big amount of information we just have clean, validated data.

### During this process i needed to do following steps:
### Rename the columns.
### Remove the unnesessory columns.
### Recheck the data types. and change them to the correct data types.
### Trim the records.
### And feature engineering to the date column



## Data Analysis

### Hour Base Analysis

Based on the hourly distribution of accidents, the highest number of accidents occur between 16:00 and 19:00, as well as around 8:00 and 9:00 in the morning. This pattern suggests that the primary reasons for these peaks could be related to people's daily routines. In the morning, individuals are likely rushing to get to work, school, or other commitments. 

 Similarly, in the evening, there is a rush to return home or pick up children. These timeframes coincide with higher traffic volumes on the roads, which in turn increases the likelihood of accidents. the data indicates that more cars on the road during these peak hours correlate with a higher incidence of accidents.

### Monthly Base Analysis :

Highest Accidents in September: The month of September has the highest number of accidents, with 17,827 incidents. This could be attributed to the return to regular routines after summer holidays, resulting in increased traffic.

June and October Peaks: June (17,666 accidents) and October (16,893 accidents) also show high numbers of accidents. These months might coincide with specific weather conditions or increased travel activities.

Spring and Summer: Accidents tend to rise in late spring and summer (May, June, July, and August), likely due to more outdoor activities, vacations, and potentially better weather leading to increased road usage.

Winter Months: Accident numbers in the winter months (January, February, and December) are relatively lower compared to the peaks in late spring and summer. However, they are still significant, possibly due to hazardous driving conditions like snow and ice. 
Numbers are lower then summer, It might be people are more carefull because of cold, Ice, visuability etc.


### Weekdays Vs Weekends

Highest Accidents on Fridays: The data shows that the highest number of accidents occur on Fridays, with a total of 28,890 accidents. This could be attributed to the end-of-week rush, where people are eager to finish their workweek and start their weekend activities.

Lowest Accidents on Sundays: Sundays have the lowest number of accidents, with 19,515 incidents. This might be due to lighter traffic and fewer people commuting for work or school.

Weekday vs. Weekend: Generally, weekdays have higher accident rates compared to weekends. This aligns with typical commuting patterns, where there are more vehicles on the road during weekdays due to work and school.


## Regional differences 

The Vlaams Gewest records the highest number of accidents and injuries, reflecting the extensive road network and population density. In contrast, the Brussels Hoofdstedelijk Gewest has the lowest figures, likely due to effective urban traffic management.

Antwerpen: Highest total accidents (32,701) and slight injuries (29,386), indicating significant traffic activity.

Brussels: Significant accidents (18,640) but relatively low fatalities (45) and serious injuries (795), likely due to effective urban traffic management.

Henegouwen: High fatality rate (307) and serious injuries (1,367), highlighting the need for safety improvements.

Other Provinces: Moderate to high accident rates and injuries, with specific provinces showing higher fatalities and serious injuries that might need targeted safety measures.



### Within Build-up Area Vs outside Buidd-up Area

Higher Accidents Within Built-up Areas:

Across most provinces, the number of accidents is higher within built-up areas compared to outside built-up areas. This trend is especially pronounced in urban regions like Brussels and Provincie Antwerpen.

**Significant Difference in Provincial Limburg:**

Provincie Limburg is an exception with more accidents outside built-up areas (8,336) compared to within built-up areas (4,582). This indicates that road safety issues in rural or less populated areas are a significant concern in Limburg.

#### Urban vs. Rural Contrast:

In densely populated provinces like Brussels and Antwerpen, a majority of accidents occur within built-up areas due to higher traffic density, more intersections, and greater pedestrian activity.

Rural provinces like Luxemburg and Waals-Brabant show fewer accidents overall, but the numbers are relatively balanced between built-up and non-built-up areas.

Provinces with High Built-up Area Accidents:

Provincie Antwerpen (18,634) and Provincie Oost-Vlaanderen (16,246) have high numbers of accidents within built-up areas, emphasizing the need for urban road safety measures.


### Overall Trends Snelwegen(90-120 km/u) Vs Autowegen(50-90 km/u)

**Autosnelweg (Highway):**

Highways account for a significant number of total accidents (13,001) but have a relatively lower fatality rate (355) compared to other road types. Serious injuries and slight injuries are also substantial on highways, indicating high-speed impacts can still result in severe consequences.

**Gewestweg, provincieweg of gemeenteweg (Regional, Provincial, or Municipal Roads):**

These roads have the highest number of total accidents (163,471), likely due to their extensive network and usage by both local and through traffic. They also show the highest numbers in all other categories: fatalities (1,539), fatalities within 30 days (2,130), serious injuries (13,864), slight injuries (147,477), and minor injuries (591). The higher numbers can be attributed to the mixed traffic conditions, varying road quality, and potential lack of stringent safety measures compared to highways.


 ### Severity of Accidents

Highways (Auto Snelwegen) report significantly lower accident numbers compared to main roads (AutoRoad). However, the relative consistency in serious injuries and fatalities highlights the need for continued safety measures on highways.

**Serious Injuries:**

Both highways and main roads report a considerable number of serious injuries, emphasizing the severity of traffic accidents on these road types. Autostrades, given their higher accident numbers, naturally report more serious injuries.

**Fatality Trends:**

The number of fatalities within 30 days of accidents is slightly higher than the immediate fatalities, indicating the critical importance of timely medical intervention and road safety measures.

 ### Light Conditions and Impact

Daylight Conditions: Most accidents occur during the day, with the highest numbers in Provincie Antwerpen, Provincie Oost-Vlaanderen, and Provincie West-Vlaanderen.

Dawn-Dusk Conditions: Accidents during dawn and dusk are fewer but still significant. Provincie Antwerpen and Provincie Oost-Vlaanderen lead in this category.

Night without Public Lighting: Fewer accidents occur at night without public lighting, with Provincie Oost-Vlaanderen and Provincie West-Vlaanderen reporting the highest numbers.

Night with Public Lighting: A considerable number of accidents happen at night with public lighting, notably in Provincie Antwerpen, Provincie Oost-Vlaanderen, and Brussels.

## Collision Types:

The year 2020 saw a noticeable reduction in accidents across most types, likely due to reduced traffic during the COVID-19 pandemic. However, numbers have since rebounded, underscoring the persistent nature of these issues.

**Side Impact (Langs opzij):** Most frequent type of collision, often occurring at intersections.

**Rear-end (Langs achteren):** Common in heavy traffic or at stoplights.

**With Pedestrian (Met een voetganger):** Significant number, particularly in urban areas.

**Against an Obstacle (Tegen een hindernis):** Both on and off the road, these collisions highlight issues with road design or driver distraction.



### Summary of the observations:

1. **Hourly Distribution of Accidents**: Accidents peak during 16:00-19:00 and around 08:00-09:00, likely due to rush hours when people are commuting to and from work and school, leading to higher traffic volumes and more accidents.

2. **Daily Distribution of Accidents**: Fridays have the highest accident rates, while Sundays have the lowest, indicating that end-of-week rush and lighter weekend traffic affect accident occurrences.

3. **Monthly Distribution of Accidents**: September records the highest number of accidents, while April has the lowest. The increase in accidents during late spring and summer months suggests more outdoor activities and vacations, leading to higher road usage.

4. **Yearly Distribution of Accidents**: A noticeable dip in total accidents in 2020 due to COVID-19 restrictions, followed by a rise in subsequent years. There is a consistent reduction in fatalities and serious injuries over time, indicating improved road safety and emergency response measures.

5. **Road Type Distribution of Accidents**: Regional, provincial, and municipal roads have the highest accident rates and associated consequences, likely due to higher traffic volumes and diverse road conditions. Highways show a lower proportion of fatalities and severe injuries.

6. **Accidents per Region**: Vlaams Gewest has the highest number of accidents and injuries, reflecting its larger population and extensive road network. Brussels Hoofdstedelijk Gewest has lower figures, likely due to effective urban traffic management.

7. **Top 10 Municipalities with the Most Accidents**: Antwerpen has the highest number of accidents, followed by Brussel and Gent, indicating significant traffic activity in these areas. Safety improvements and infrastructure enhancements are essential in these municipalities to reduce accidents and injuries.



### Recommendations

**Urban Road Safety Measures**
Improve pedestrian, Bicycle road, parking infrastructure and traffic management. Redesign intersections to reduce accidents within built-up areas.

**Rural Road Safety Initiatives**
Address specific challenges like speeding, visibility, and road design improvements.

**Enhanced Road Safety Measures**
Focus on highways and main roads to reduce accidents, serious injuries, and fatalities.

**Public Awareness Campaigns**
There are a few campaigns (Bob, Speed) we can see in Belgium, But may be this is not enough? People still do dirink and drive, don't follow the speed limit, respect everyone on the street, Give priority and get priority. This are the thinks public must be aware with and from government side also need to do more controls and awareness campaigns. Increase awareness about safe driving practices, especially in high-risk areas.


### Conclusion
This project provides valuable insights into the factors influencing traffic accidents in Belgium. By focusing on high-risk areas and implementing targeted safety measures, we can work towards reducing the number and severity of traffic accidents, ultimately making the roads safer for everyone.
