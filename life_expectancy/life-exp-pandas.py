"""
File: life-exp-pandas.py
Author: Nathan Johnston

Objective: Analysis of a census data

"""
import pandas

census_file = "life_expectancy\\life-expectancy.csv"

census = pandas.read_csv(census_file)

print(census)
