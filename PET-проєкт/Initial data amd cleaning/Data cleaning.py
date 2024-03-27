#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd


# In[81]:


import pandas as pd

# Завантаження файлу saas.csv
saas = pd.read_csv('C:\\Users\\Nataliia\\Desktop\\saas.csv', sep=';')

# Видалення рядків зі значеннями NaN
saas_cleaned = saas.dropna()

# Виведення оновленого DataFrame
print(saas_cleaned)


# In[82]:


import pandas as pd

# Завантаження файлів saas.csv та координат
saas = pd.read_csv('C:\\Users\\Nataliia\\Desktop\\saas.csv')

# Створення DataFrame з координатами
Country = [
    "Argentina", "Australia", "Austria", "Belgium", "Brazil", "Canada", "Chile", "China", "Colombia", "Costa Rica",
    "Croatia", "Czech Republic", "Denmark", "Egypt", "Finland", "France", "Germany", "Greece", "Iceland", "India",
    "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Luxembourg", "Mexico", "Netherlands", "New Zealand", "Norway",
    "Philippines", "Poland", "Portugal", "Qatar", "Russia", "Saudi Arabia", "Singapore", "Slovenia", "South Africa",
    "South Korea", "Spain", "Sweden", "Taiwan", "Turkey", "Ukraine", "United Arab Emirates", "United Kingdom", "United States"
]

latitudes = [
    -38.4161, -25.2744, 47.5162, 50.5039, -14.2350, 56.1304, -35.6751, 35.8617, 4.5709, 9.7489,
    45.1000, 49.8175, 56.2639, 26.8206, 61.9241, 46.6034, 51.1657, 39.0742, 64.9631, 20.5937,
    -0.7893, 53.4129, 31.0461, 41.8719, 36.2048, 49.8153, 23.6345, 52.1326, -40.9006, 60.4720,
    12.8797, 51.9194, 39.3999, 25.3548, 61.5240, 23.8859, 1.3521, 46.1512, -30.5595, 35.9078,
    40.4637, 60.1282, 23.6978, 38.9637, 48.3794, 23.4241, 55.3781, 37.0902
]

longitudes = [
    -63.6167, 133.7751, 14.5501, 4.4699, -51.9253, -106.3468, -71.5430, 104.1954, -74.2973, -83.7534,
    15.2000, 15.4720, 9.5018, 30.8025, 25.7482, 1.8883, 10.4515, 21.8243, -19.0208, 78.9629,
    113.9213, -8.2439, 34.8516, 12.5674, 138.2529, 6.1296, -102.5528, 5.2913, 174.8860, 8.4689,
    121.7740, 19.1451, -8.2245, 51.1839, 105.3188, 45.0792, 103.8198, 14.9955, 22.9375, 127.7669,
    -3.7492, 18.6435, 120.9605, 35.2433, 31.1656, 53.8478, -3.4360, -95.7129
]

coordinates = pd.DataFrame({'Country': Country, 'Latitude': latitudes, 'Longitude': longitudes})


# Об'єднання даних з saas_cleaned та coordinates за полем "Country"
merged_data = pd.merge(saas_cleaned, coordinates, on='Country')

merged_data['Latitude'] = merged_data['Latitude'].astype(float)
merged_data['Longitude'] = merged_data['Longitude'].astype(float)

# Виведення результату
print(merged_data)


# In[83]:


import pandas as pd

# Зміна типів даних для стовпців
merged_data['Order ID'] = merged_data['Order ID'].astype(str)
merged_data['Date Key'] = merged_data['Date Key'].astype(int)
merged_data['Contact Name'] = merged_data['Contact Name'].astype(str)
merged_data['Country'] = merged_data['Country'].astype(str)
merged_data['City'] = merged_data['City'].astype(str)
merged_data['Region'] = merged_data['Region'].astype(str)
merged_data['Subregion'] = merged_data['Subregion'].astype(str)
merged_data['Customer'] = merged_data['Customer'].astype(str)
merged_data['Customer ID'] = merged_data['Customer ID'].astype(int)
merged_data['Industry'] = merged_data['Industry'].astype(str)
merged_data['Segment'] = merged_data['Segment'].astype(str)
merged_data['Product'] = merged_data['Product'].astype(str)
merged_data['License'] = merged_data['License'].astype(str)
merged_data['Sales'] = pd.to_numeric(merged_data['Sales']).astype(float)
merged_data['Quantity'] = pd.to_numeric(merged_data['Quantity']).astype(float)
merged_data['Discount'] = pd.to_numeric(merged_data['Discount']).astype(float)
merged_data['Profit'] = merged_data['Profit'].astype(float)
merged_data['Order Date'] = pd.to_datetime(merged_data['Order Date'], format='%d.%m.%Y')
merged_data['is Refunded'] = merged_data['is Refunded'].astype(bool)
merged_data['Latitude'] = merged_data['Latitude'].astype(float)
merged_data['Longitude'] = merged_data['Longitude'].astype(float)

# Виведення оновленого DataFrame
print(merged_data)


# In[80]:


# Збереження DataFrame у файлі CSV
merged_data.to_csv('merged_data2.csv', index=False)


# In[85]:


import pandas as pd

# Завантаження файлу saas.csv
saas = pd.read_csv('C:\\Users\\Nataliia\\Desktop\\saas.csv', sep=';')

# Видалення рядків зі значеннями NaN
saas_cleaned = saas.dropna()

import pandas as pd

# Завантаження файлів saas.csv та координат
saas = pd.read_csv('C:\\Users\\Nataliia\\Desktop\\saas.csv')

# Створення DataFrame з координатами
Country = [
    "Argentina", "Australia", "Austria", "Belgium", "Brazil", "Canada", "Chile", "China", "Colombia", "Costa Rica",
    "Croatia", "Czech Republic", "Denmark", "Egypt", "Finland", "France", "Germany", "Greece", "Iceland", "India",
    "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Luxembourg", "Mexico", "Netherlands", "New Zealand", "Norway",
    "Philippines", "Poland", "Portugal", "Qatar", "Russia", "Saudi Arabia", "Singapore", "Slovenia", "South Africa",
    "South Korea", "Spain", "Sweden", "Taiwan", "Turkey", "Ukraine", "United Arab Emirates", "United Kingdom", "United States"
]

latitudes = [
    -38.4161, -25.2744, 47.5162, 50.5039, -14.2350, 56.1304, -35.6751, 35.8617, 4.5709, 9.7489,
    45.1000, 49.8175, 56.2639, 26.8206, 61.9241, 46.6034, 51.1657, 39.0742, 64.9631, 20.5937,
    -0.7893, 53.4129, 31.0461, 41.8719, 36.2048, 49.8153, 23.6345, 52.1326, -40.9006, 60.4720,
    12.8797, 51.9194, 39.3999, 25.3548, 61.5240, 23.8859, 1.3521, 46.1512, -30.5595, 35.9078,
    40.4637, 60.1282, 23.6978, 38.9637, 48.3794, 23.4241, 55.3781, 37.0902
]

longitudes = [
    -63.6167, 133.7751, 14.5501, 4.4699, -51.9253, -106.3468, -71.5430, 104.1954, -74.2973, -83.7534,
    15.2000, 15.4720, 9.5018, 30.8025, 25.7482, 1.8883, 10.4515, 21.8243, -19.0208, 78.9629,
    113.9213, -8.2439, 34.8516, 12.5674, 138.2529, 6.1296, -102.5528, 5.2913, 174.8860, 8.4689,
    121.7740, 19.1451, -8.2245, 51.1839, 105.3188, 45.0792, 103.8198, 14.9955, 22.9375, 127.7669,
    -3.7492, 18.6435, 120.9605, 35.2433, 31.1656, 53.8478, -3.4360, -95.7129
]

coordinates = pd.DataFrame({'Country': Country, 'Latitude': latitudes, 'Longitude': longitudes})


# Об'єднання даних з saas_cleaned та coordinates за полем "Country"
merged_data = pd.merge(saas_cleaned, coordinates, on='Country')

merged_data['Latitude'] = merged_data['Latitude'].astype(float)
merged_data['Longitude'] = merged_data['Longitude'].astype(float)

import pandas as pd

# Зміна типів даних для стовпців
merged_data['Order ID'] = merged_data['Order ID'].astype(str)
merged_data['Date Key'] = merged_data['Date Key'].astype(int)
merged_data['Contact Name'] = merged_data['Contact Name'].astype(str)
merged_data['Country'] = merged_data['Country'].astype(str)
merged_data['City'] = merged_data['City'].astype(str)
merged_data['Region'] = merged_data['Region'].astype(str)
merged_data['Subregion'] = merged_data['Subregion'].astype(str)
merged_data['Customer'] = merged_data['Customer'].astype(str)
merged_data['Customer ID'] = merged_data['Customer ID'].astype(int)
merged_data['Industry'] = merged_data['Industry'].astype(str)
merged_data['Segment'] = merged_data['Segment'].astype(str)
merged_data['Product'] = merged_data['Product'].astype(str)
merged_data['License'] = merged_data['License'].astype(str)
merged_data['Sales'] = pd.to_numeric(merged_data['Sales']).astype(float)
merged_data['Quantity'] = pd.to_numeric(merged_data['Quantity']).astype(float)
merged_data['Discount'] = pd.to_numeric(merged_data['Discount']).astype(float)
merged_data['Profit'] = merged_data['Profit'].astype(float)
merged_data['Order Date'] = pd.to_datetime(merged_data['Order Date'], format='%d.%m.%Y')
merged_data['is Refunded'] = merged_data['is Refunded'].astype(bool)
merged_data['Latitude'] = merged_data['Latitude'].astype(float)
merged_data['Longitude'] = merged_data['Longitude'].astype(float)

# Виведення оновленого DataFrame
print(merged_data)

# Збереження DataFrame у файлі CSV
merged_data.to_csv('merged_data.csv', index=False)


# In[ ]:




