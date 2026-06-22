Netflix Content Analysis Dashboard

Project Overview

This project performs Exploratory Data Analysis (EDA) on the Netflix Titles dataset and presents insights through an interactive Streamlit dashboard. The analysis focuses on content distribution, genres, ratings, countries, directors, actors, and content trends over time.

Objectives

- Analyze Netflix content using Python.
- Perform data cleaning and preprocessing.
- Generate meaningful visualizations.
- Build an interactive dashboard using Streamlit.
- Extract insights from Netflix content data.

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

Dataset

Dataset: Netflix Titles Dataset

The dataset contains information about:

- Title
- Type (Movie / TV Show)
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genre

Data Cleaning

The following preprocessing steps were performed:

- Handled missing values.
- Filled null values in Director, Cast, Country, Rating, and Duration columns.
- Converted date columns into proper datetime format.
- Removed inconsistencies in the dataset.

Exploratory Data Analysis

The following analyses were performed:

1. Movies vs TV Shows Distribution
2. Top 10 Countries
3. Top 10 Genres
4. Content Added Over Years
5. Content Rating Distribution
6. Content Released Per Year
7. Top 10 Directors
8. Top 10 Actors
9. Movie Duration Distribution
10. Correlation and Trend Analysis

Dashboard Features

- Interactive Streamlit Dashboard
- Content Type Filter (Movie / TV Show)
- KPI Cards:
  - Total Titles
  - Total Movies
  - Total TV Shows
- Multiple Interactive Visualizations
- Clean and User-Friendly Interface

Key Insights

- Movies are more numerous than TV Shows on Netflix.
- The United States contributes the highest amount of content.
- International Movies and Dramas are among the most common genres.
- TV-MA is one of the most frequent content ratings.
- Netflix content additions increased significantly after 2015.
- Most movies have durations between 80 and 120 minutes.

Project Structure

Netflix_Data_Analysis/

├── Dataset/

│   └── netflix_titles.csv

├── Notebook/

│   └── netflix_analysis.py

├── app.py

├── README.md

└── Graph Images

How to Run

1. Install dependencies:

pip install pandas numpy matplotlib seaborn streamlit

2. Run the dashboard:

python -m streamlit run app.py

Future Enhancements

- Country-based filters
- Genre-based filters
- Recommendation System
- Advanced Dashboard Styling
- Deployment on Streamlit Cloud

Author

Akhila Singam