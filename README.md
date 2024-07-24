# Data Exploration, Cleansing, and Preparation

## Asg1

The goal of this task is to read in a `TXT` file containing data in `XML` format and export it into a `JSON` file.   
The approach to this task is to first split the data by `<assignment-entry>`, then extract the information into a DataFrame for re-formatting or merging. The DataFrame would then be transferred into a `JSON` file. The data file contains 6338 records of property assignments, including assignors and assignees.

## Part 1: Data Cleansing and Quality Assessment

### Dataset Overview

- **Context**: Food Delivery data from a restaurant in Melbourne, Australia.
- **Dimensions**: 500 rows x 12 columns.
- **Target Variable**: Delivery fee.

### Tasks and Methodologies

1. **Dirty Data Detection and Fixing**:
    - **Objective**: Ensure data aligns with the schema by detecting and correcting errors.
    - **Process**: 
        - Validate data types and constraints for each column.
        - Identify and correct inconsistencies and inaccuracies.

2. **Missing Data Imputation**:
    - **Objective**: Impute missing values and evaluate the accuracy of the imputation.
    - **Process**:
        - Identify missing values across the dataset.
        - Apply various imputation methods (mean, median, mode, etc.).
        - Evaluate imputation accuracy using R² (coefficient of determination).

3. **Outlier Detection and Removal**:
    - **Objective**: Detect and remove outliers, then compare visualizations before and after removal.
    - **Process**:
        - Use statistical methods (IQR, Z-score) to identify outliers.
        - Remove detected outliers.
        - Visualize data distribution before and after outlier removal.

## Part 2: Data Preparation for Linear Modeling

### Dataset Overview

- **Context**: Suburb data including house number, house price, population, and related demographic information.
- **Dimensions**: 202 rows x 8 columns.
- **Target Variable**: Median house price.

### Tasks and Methodologies

1. **Data Transformation**:
    - **Objective**: Enhance relationships between features and the target variable.
    - **Approaches**:
        - Log Transformation
        - Power Transformation
        - Square Root Transformation
        - Inverse Transformation
        - Inverse Square Root Transformation
        - Inverse Square Transformation

2. **Data Scaling**:
    - **Objective**: Ensure the same range across all features.
    - **Approaches**:
        - Min-Max Scaling
        - Normalization

### Implementation Process

1. **Data Type Conversion**:
    - Convert all columns (except 'suburb' and 'municipality') to numerical types for further exploration and analysis.

2. **Transformation and Scaling**:
    - Apply different transformation techniques to various columns.
    - Scale the transformed data to maintain a consistent range across features.

## Summary

The detailed steps and results for each part are documented in the following sections. This document serves as a comprehensive guide to understanding the data exploration, cleansing, and preparation processes undertaken in these tasks.
