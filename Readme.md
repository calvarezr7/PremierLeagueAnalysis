# Data Exploratory Analysis Project

## Description

This project conducts an exploratory data analysis (EDA) on a dataset downloaded from Kaggle. It includes data collection, cleaning, visualization, and modeling to extract meaningful insights.

## Project Structure

The project follows best practices to keep files organized, maintainable, and scalable.

```
PremierLeague/
│-- data/
│   ├── raw/              # Original unprocessed data
│   ├── processed/        # Cleaned and transformed data
│
│-- notebooks/
│   ├── 01_preprocessing.ipynb  # Data delimited and selected
│   ├── 02_exploratory_analysis.ipynb  # Exploratory analysis
│   ├── 03_data_processing.ipynb  # Data transformation / visualizations
│
│-- src/
│   ├── download_data.py  # Script for data loading from Kaggle
│
│-- reports/
│   ├── figures/  # Generated visualizations
│   ├── summary.pdf  # Analysis summary
│
│-- docs/  # Project documentation
│
│-- .gitignore  # Files and folders to exclude from version control
│-- README.md  # General project documentation
```


## Objectives

Objectives of the project: 

### Insights : 
- Which teams have been the most consistent in their performance over the last 10 years?
- Which teams have the most comebacks (wins after trailing)?
- How does playing at home or away affect the results?

### Visualizations :
- A simple dashboard for teams performance

### Models: 
- Pronostic of goals in the current season

