
🏠 Housing Market Analysis using Tableau
📌 Project Overview

This project focuses on analyzing housing market data to uncover insights about property prices, renovation impact, and housing characteristics. Using Tableau, the dataset was cleaned, prepared, and visualized to help stakeholders better understand housing trends and support data-driven decision making.

The project demonstrates how data visualization can transform raw housing data into meaningful insights for real estate analysts, marketing teams, and company executives.

🎯 Project Objectives

The primary objectives of this project are:

Analyze housing sales data to identify trends and patterns.

Understand how renovation affects house prices.

Study the relationship between house age and property features.

Visualize housing characteristics such as bedrooms, bathrooms, and floors.

Build an interactive Tableau dashboard for better market insights.

📊 Dataset Information

Dataset Name: Housing_Data.csv
Total Records: 21,609
Total Columns: 31

The dataset contains detailed information about housing properties including price, structure, renovation status, and location attributes.

Key Attributes in Dataset
Attribute	Description
Sale Price	Selling price of the house
Bedrooms	Number of bedrooms
Bathrooms	Number of bathrooms
Flat Area	Living area of the house (sqft)
Lot Area	Total lot area (sqft)
Floors	Number of floors
House Age	Age of the house
Years Since Renovation	Years passed since last renovation
Above Ground Area	Area of house above basement
Basement Area	Basement size
Latitude	Geographic coordinate
Longitude	Geographic coordinate
Property Condition	Condition category of the house
Waterfront View	Whether the property has waterfront view
Zipcode Groups	Location category
🧹 Data Cleaning and Preparation

Data cleaning was performed in Tableau Public to ensure the dataset is structured and ready for visualization.

Data Review

Verified dataset structure and data types.

Checked value ranges and distributions.

Explored dataset attributes to understand housing characteristics.

Field Renaming

Several columns were renamed to improve readability.

Original Column Name	Updated Name
No of Bedrooms	Bedrooms
No of Bathrooms	Bathrooms
Flat Area (in Sqft)	Flat Area
Lot Area (in Sqft)	Lot Area
No of Floors	Floors
Area of the House from Basement (in Sqft)	Above Ground Area
Data Structuring

Fields were organized into Dimensions and Measures.

Dimensions

Bedrooms

Bathrooms

Floors

Renovation Status

Property Condition

Zipcode Groups

Measures

Sale Price

Flat Area

Lot Area

Basement Area

House Age

Latitude

Longitude

Data Validation

Verified record counts and dataset integrity.

Checked for missing or invalid values.

Confirmed numerical formatting for analytical fields.

📈 Data Visualizations

The following visualizations were created in Tableau:

1️⃣ Overall Data Overview

Displays summary statistics of the dataset such as:

Total number of houses

Average sale price

Total basement area

This provides a quick overview of the housing dataset.

2️⃣ Total Sales by Years Since Renovation

A histogram showing how sales prices vary based on the number of years since a house was renovated.

This helps determine whether recently renovated houses have higher sale prices.

3️⃣ Distribution of House Age by Renovation Status

A pie chart illustrating the distribution of houses by age group and renovation status.

This visualization highlights the proportion of renovated vs non-renovated properties.

4️⃣ House Age Distribution by Bedrooms, Bathrooms, and Floors

A grouped bar chart analyzing how house age relates to structural features such as:

Bedrooms

Bathrooms

Floors

This helps identify patterns in housing characteristics over time.

📊 Dashboard Design

The Tableau dashboard integrates multiple visualizations into an interactive interface.

Features include:

Interactive filters

Clear layout for key insights

Visual comparison of housing attributes

User-friendly interface for data exploration

🧠 Insights Expected from Analysis

The project helps answer questions such as:

Do renovated houses sell at higher prices?

How does house age affect property characteristics?

What types of houses dominate the housing market?

How do structural features influence housing prices?

🛠 Tools and Technologies
Tool	Purpose
Tableau Public	Data visualization and dashboard creation
GitHub	Version control and project collaboration
CSV Dataset	Housing data source
📁 Project Repository Structure
housing-tableau-project
│
├── data
│   └── Housing_Data.csv
│
├── tableau
│   └── housing_cleaned.twbx
│
└── README.md
👥 Team Contributions
Data Cleaning & Preparation

Dataset exploration

Column renaming

Structuring dimensions and measures

Data validation

Visualization and Dashboard

Tableau visualizations

Dashboard design

Storyboard creation

Deployment

Dashboard publishing

Web integration using Flask

🚀 Future Improvements

Potential enhancements for this project include:

Integration with real-time housing data

Machine learning models for price prediction

Geographic mapping of housing prices

Advanced interactive dashboards

📌 Conclusion

This project demonstrates how Tableau can be used to analyze housing data and uncover meaningful insights. Through effective data cleaning, visualization, and dashboard development, the project provides valuable perspectives on housing market dynamics.

📜 License

This project is for educational and analytical purposes.