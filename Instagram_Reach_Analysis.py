import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

data = pd.read_csv("https://github.com/bmpafe1/Python/blob/151f695d5e4dae9b3eca1f9883fae943c9279a0d/Instagram_data.csv?raw=true", encoding = 'latin1')

#Distribution of impressions received from home:
plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
sns.distplot(data['From Home'])
plt.show()

#Distribution of the impressions from hashtags:
plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()

#Distribution of impressions received from the explore section of Instagram:
plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Explore")
sns.distplot(data['From Explore'])
plt.show()

#Percentage of impressions got from various sources on Instagram
home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ['From Home','From Hashtags','From Explore','Other']
values = [home, hashtags, explore, other]

fig = px.pie(data, values=values, names=labels, title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()

#The most used words in the caption of my Instagram posts:
text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("The most used words in the caption of my Instagram posts")
plt.show()

#The most used hashtags in my Instagram posts:
text = " ".join(i for i in data.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("The most used hashtags in my Instagram posts")
plt.show()

#The relationship between the number of likes and the number of impressions on my Instagram posts:
figure = px.scatter(data_frame = data, x="Impressions", y="Likes", size="Likes", trendline="ols", title = "Relationship Between Likes and Impressions")
figure.show()

#The relationship between the number of comments and the number of impressions on my Instagram posts:
figure = px.scatter(data_frame = data, x="Impressions", y="Comments", size="Comments", trendline="ols", title = "Relationship Between Comments and Total Impressions")
figure.show()

#The relationship between the number of shares and the number of impressions:
figure = px.scatter(data_frame = data, x="Impressions", y="Shares", size="Shares", trendline="ols", title = "Relationship Between Shares and Total Impressions")
figure.show()

#The relationship between the number of saves and the number of impressions:
figure = px.scatter(data_frame = data, x="Impressions", y="Saves", size="Saves", trendline="ols", title = "Relationship Between Post Saves and Total Impressions")
figure.show()

#Analyzing Conversion Rate
conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)

#The relationship between the total profile visits and the number of followers gained from all profile visits:
figure = px.scatter(data_frame = data, x="Profile Visits", y="Follows", size="Follows", trendline="ols", title = "Relationship Between Profile Visits and Followers Gained")
figure.show()

#INSTAGRAM REACH PREDICTION MODEL

#STEP 1: Split data into training and test sets before training the model:
x = np.array(data[['Likes', 'Saves', 'Comments', 'Shares', 'Profile Visits', 'Follows']])
y = np.array(data["Impressions"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

#Train the machine learning model to predict the reach of an Instagram post using Python:
model = PassiveAggressiveRegressor()
model.fit(xtrain, ytrain)
model.score(xtest, ytest)

#Now let’s predict the reach of an Instagram post by giving inputs to the machine learning model:
# Features = [['Likes','Saves', 'Comments', 'Shares', 'Profile Visits', 'Follows']]
features = np.array([[282.0, 233.0, 4.0, 9.0, 165.0, 54.0]])
model.predict(features)