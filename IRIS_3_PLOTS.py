# -*- coding: utf-8 -*-
"""Assn_10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mKvvJhUEk6jexvh1feCwh1YuzIVpDhIJ

# Assignment No 10

# Problem Statement:
Data Visualization III
Download    the    Iris    flower    dataset    or    any    other    dataset    into    a    DataFrame.    (e.g., https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as:
1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
2. Create a histogram for each feature in the dataset to illustrate the feature distributions.
3. Create a box plot for each feature in the dataset.
4. Compare distributions and identify outliers.
"""

import seaborn as sns
import matplotlib.pyplot as plt

dataset = sns.load_dataset("iris")
dataset.head()

fig,axes = plt.subplots(2,2,figsize=(16,9))
sns.boxplot(y='sepal_length', x='species', data=dataset, ax=axes[0,0])
sns.boxplot(y='sepal_width', x='species', data=dataset, ax=axes[0,1])
sns.boxplot(y='petal_length', x='species', data=dataset, ax=axes[1,0])
sns.boxplot(y='petal_width', x='species', data=dataset, ax=axes[1,1])

fig,axes = plt.subplots(2,2,figsize=(16,9))
sns.histplot(dataset['sepal_length'], ax = axes[0,0])
sns.histplot(dataset['sepal_width'], ax = axes[0,1])
sns.histplot(dataset['petal_length'], ax = axes[1,0])
sns.histplot(dataset['petal_width'], ax = axes[1,1])

fig,axes = plt.subplots(2,2,figsize=(16,9))
sns.distplot(dataset['sepal_length'], ax = axes[0,0])
sns.distplot(dataset['sepal_width'], ax = axes[0,1])
sns.distplot(dataset['petal_length'], ax = axes[1,0])
sns.distplot(dataset['petal_width'], ax = axes[1,1])