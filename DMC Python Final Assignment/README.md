# Final Project: Analysis of Departmental Indicators

This project focuses on the cleaning and analysis of data extracted from the web, with the goal of evaluating different departmental indicators. The following outlines the tasks performed in the final project for the DMC Python course.

## Objectives

1. **Clean the extracted table from the web:**
   - Clean the columns and standardize them according to defined criteria.
   - Remove unnecessary or null columns.
   - Verify and assign the correct data type to each column.
   - Save the result in a Parquet file named `indicadores_departamentales.parquet`.
   - **[OPTIONAL]** Create an SQLite database using SQLAlchemy and store the cleaned table in it.

2. **Calculate population density:**
   - Calculate how many people there are per square kilometer in each department using the formula:  
     \[
     \text{Density} = \frac{\text{Census Population}}{\text{Area}}
     \]

3. **Comparison of areas:**
   - Assess how small the area of Callao, Metropolitan Lima, and Lima Provinces is compared to the department of Amazonas using the formula:  
     \[
     \text{Ratio} = \frac{\text{Areas of Callao + Metropolitan Lima + Lima Provinces}}{\text{Area of Amazonas}}
     \]

4. **Analysis of population growth:**
   - Determine the growth of the population according to the 2022 estimate compared to the census population in 2017.


## Contributions

Contributions are always welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.