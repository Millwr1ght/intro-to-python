"""
File: life-exp-pandas.py
Author: Nathan Johnston

Objective: Analysis of a census data

"""
import pandas
import matplotlib.pyplot as plt

census_file = "life_expectancy\\life-expectancy.csv"

census = pandas.read_csv(census_file)

print(census)
