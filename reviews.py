import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

points_avg_country = reviews.groupby('country')['points'].mean().round(1)
review_sum_country = reviews.country.value_counts()

result = pd.merge(review_sum_country, points_avg_country, on='country')

df = pd.DataFrame(result)
df.to_csv('data/reviews-per-country.csv')