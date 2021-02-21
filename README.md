# Project-5: SNOTEL Water Level Analysis

## Problem Statement
The National Resources Conservation Service keeps track of precipitation levels in water basins across the Western United States using an automated system known as SNOTEL. This information is critical for resource management and provides insight on the climate status in the regions where the data is gathered. Understanding what areas may be experiencing abnormalities can be key  for planning resource management operations. Our goal is to determine if we can produce a model to predict precipitation levels in a water basin using data gathered from NRCS SNOTEL sites. 


----------------------------

## Background
#### SNOTEL
The Natural Resources Conservation Service (NRCS) uses an automated system to collect snowpack and climate data in the Western United States known as SNOTEL (SNOwpack TELemetry). Growing from a manual measurement system SNOTEL has been reliably collecting data to produce water supply forecasts and support resource management activities since 1980. SNOTEL uses meteor burst communications to collect and communicate data in near real time without the use of satellites. There are more than 730 SNOTEL sites in 11 states, all designed to operate without maintenance for a year as they are typically in remote locations and maintenance trips can involve long hikes or helicopter trips. The NRCS National Water and Climate Center in Portland, Oregon houses the central computer that controls operation of the sites and receives the data gathered.

|                  More information on SNOTEL can be found at the following links                  |
|:------------------------------------------------------------------------------------------------:|
| [SNOTEL Data Collection Network Fact Sheet](https://www.wcc.nrcs.usda.gov/factpub/sntlfct1.html) |
| [SNOTEL Brochure](https://www.wcc.nrcs.usda.gov/snotel/snotel_brochure.pdf)                      |
| [Snow Telemetry and Snow Course Data and Products](https://www.wcc.nrcs.usda.gov/snow/)          |

Our main focus was to look at the current reported precipitation level as well as the precipitation year to date for each site.

--------------------------
## Data
Data used contains data from SNOTEL sites in the Columbia River Basin on February 10th from the years 1990 - 2021.

SNOTEL Snow/Precipitation Update Reports were gathered [here](https://wcc.sc.egov.usda.gov/reports/SelectUpdateReport.html).

#### Data Dictionary
|Feature                 |Description                                             |
|------------------------|--------------------------------------------------------|
| Lat                    | Decimal Latitude of SNOTEL Site                        |
| Long                   | Decimal Latitude of SNOTEL Site                        |
| YYYYMMDD               | Date of Observation                                    |
| Basin_name             | SNOTEL Site Sub-basin Name                             |
| Station_id             | SNOTEL System Identification Code                      |
| Acton_id               | Snow Survey Program ACTON Code                         |
| Station_name           | SNOTEL Station Name                                    |
| Elevation              | SNOTEL Site Elevation (feet)                           |
| Wteq_amt               | Current Snow Water Equivalent(inches)                  |
| Wteq_med               | Snow Water Equivalent Median (inches)                  |
| Wteq_amt_pct_med       | Current Snow Water Equivalent as Percent of Median     |
| Wteq_amt_pct_med_flag  | Snow Water Equivalent Validity Code                    |
| Prec_wytd_amt          | Water Year to Date Precipitation (inches)              |
| Prec_wytd_avg          | Water Year to Date Precipitation Average (inches)      |
| Prec_wytd_pctavg       | Water Year to Date Precipitation as Percent of Average |
| Prec_wytd_pct_avg_flag | Water Year to Date Precipitation Validity Code         |

-------------------------
## Analysis


-------------------------
## Conclusions