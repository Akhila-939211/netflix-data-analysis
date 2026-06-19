import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Load Dataset
# -------------------------
df = pd.read_csv("../Dataset/netflix_titles.csv")

# -------------------------
# 2. Basic Overview
# -------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values (Before Cleaning):")
print(df.isnull().sum())

# -------------------------
# 3. Data Cleaning
# -------------------------
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = df['date_added'].fillna("Not Available")
df['rating'] = df['rating'].fillna("Not Rated")
df['duration'] = df['duration'].fillna("Not Available")

print("\nMissing Values (After Cleaning):")
print(df.isnull().sum())

# -------------------------
# 4. Movies vs TV Shows
# -------------------------
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# -------------------------
# 5. Top 10 Countries
# -------------------------
plt.figure(figsize=(10,5))

df['country'] = df['country'].fillna("Unknown")

df['country'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("../Images/top_10_countries.png")
plt.show()

# -------------------------
# 6. Top 10 Genres
# -------------------------
plt.figure(figsize=(10,5))
genres = df['listed_in'].dropna().str.split(', ').explode()
genres.value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# -------------------------
# 7. Content Added Over Years
# -------------------------

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['year_added'] = df['date_added'].dt.year

plt.figure(figsize=(10,5))

df['year_added'].dropna().value_counts().sort_index().plot(kind='line')

plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Count")

plt.savefig("../Images/content_added_over_years.png")
plt.show()