# Long-Term Unemployment Analysis
# **Project:** Week 5 & 6 Data Visualization Assignment

## Project Overview
# This notebook analyzes the `LongTermUnemployment.xlsx` dataset. 
# The goal is to explore how long-term unemployment changed between 2005 and 2015
# understand the demographic breakdown and analyze the volatility of the job market. 
# Files are read from the `data/` directory and 
# visualizations are exported to the `output/` directory 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory if it doesnt exist
os.makedirs('output', exist_ok=True)

# Load the dataset from the data folder
file_path = '/home/rayudu/otherwork_assignment_all_jobs/Todo/Assignmet_5/data/LongTermUnemployment.xlsx'
df = pd.read_excel(file_path)

# Convert the 'Period' column to datetime for proper sorting
df['Period'] = pd.to_datetime(df['Period'])

df.head()

## 1. Line Plot: Total Long Term Unemployed Over Time

# Group by Period and sum the unemployed counts
total_unemployed_time = df.groupby('Period')['Unemployed'].sum().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(total_unemployed_time['Period'], total_unemployed_time['Unemployed'], 
         marker='', linestyle='-', linewidth=2.5, color='#1f77b4')

ax1.set_title('Total Long Term Unemployment Over Time', fontsize=16)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Persons', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)

# Format y axis to show plain numbers 
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.savefig('output/Total_Long_Term_Unemployment_Over_Time_line_plot.png', transparent=False, dpi=300, bbox_inches='tight', facecolor='white')



## 2. Bar Plot: Unemployment by Age and Gender

# Group by Age and Gender, then calculate the mean unemployment
demo_df = df.groupby(['Age', 'Gender'])['Unemployed'].mean().unstack()

# Reorder the age groups logically
age_order = ['16 to 19 years', '20 to 24 years', '25 to 34 years', 
             '35 to 44 years', '45 to 54 years', '55 to 64 years', '65 years and over']
demo_df = demo_df.reindex(age_order)

# Shorten labels for the chart
short_labels = ['16-19', '20-24', '25-34', '35-44', '45-54', '55-64', '65+']
x = np.arange(len(short_labels))
width = 0.35

fig2, ax2 = plt.subplots(figsize=(10, 6))

# Plot bars for Men and Women
bars1 = ax2.bar(x - width/2, demo_df['Men'], width, label='Men', color='#2ca02c')
bars2 = ax2.bar(x + width/2, demo_df['Women'], width, label='Women', color='#ff7f0e')

ax2.set_title('Average Long Term Unemployment by Age and Gender', fontsize=16)
ax2.set_xlabel('Age Group', fontsize=14)
ax2.set_ylabel('Number of Persons', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels(short_labels)
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Format y-axis
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.savefig('output/Average_Long_Term_Unemploymentbar_plot.png', transparent=False, dpi=300, bbox_inches='tight', facecolor='white')


## 3. Scatter Plot: Volatility Analysis

# Calculate month over month change
total_unemployed_time['MoM_Change'] = total_unemployed_time['Unemployed'].diff()

# Drop the  NaN value
volatility_df = total_unemployed_time.dropna()

fig3, ax3 = plt.subplots(figsize=(10, 6))

# Plot actual data instead of np.random
ax3.scatter(volatility_df['Unemployed'], volatility_df['MoM_Change'], 
            alpha=0.6, s=60, color='#d62728', edgecolor='black')

ax3.set_title('Volatility in Long Term Unemployment', fontsize=16)
ax3.set_xlabel('Total Unemployed (Persons)', fontsize=14)
ax3.set_ylabel('Month over Month Change (Persons)', fontsize=14)
ax3.grid(True, linestyle='--', alpha=0.6)

# Add a horizontal line at 0 for reference
ax3.axhline(0, color='black', linewidth=1, linestyle='--')

ax3.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.savefig('output/Volatility_in_Long_Term_Unemployment_scatter_plot.png', transparent=False, dpi=300, bbox_inches='tight', facecolor='white')
