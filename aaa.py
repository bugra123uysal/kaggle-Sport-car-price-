import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

car=pd.read_csv("C:\\Users\\buğra\\Desktop\\Sport car price.csv",delimiter=";")

print(car.columns)

mbg=car.sort_values('Horsepower', ascending=True)
mtork=car.sort_values('Torque (lb-ft)', ascending=True)

aau=mbg.head()

plt.bar('Car Model','Horsepower'  ,data=aau)
plt.title("the highest horsepower")
plt.grid(True)
plt.xticks(rotation=90)
plt.show()

tto=mtork.head()
plt.bar('Car Model','Horsepower'  ,data=tto)
plt.title("the highest horsepower")
plt.grid(True)
plt.show()


bm=car[car['Car Make'] == 'BMW']
p=car[car['Car Make']=='Porsche']
l=car[car['Car Make']=='Lamborghini' ]
m=car[car['Car Make']== 'McLaren']
k=car[car['Car Make']== 'Koenigsegg']



"""
sns.countplot(x='Car Make' , data=car )
plt.xticks(rotation=90)
plt.show()

sns.countplot(x='Car Model' , data=car )
plt.xticks(rotation=90)
plt.show()
  
sns.scatterplot(x='Horsepower', y='Torque (lb-ft)', data=car)
plt.xticks(rotation=90)
plt.show()

ff=car['Price (in USD)']
aa=car['Car Make']

sns.countplot(x='Car Make', hue='Car Model'  , data=bm)
plt.title("a")
plt.show()


plt.bar('Car Model','Price (in USD)', data=p )
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.grid(True)
plt.title("Porsche")
plt.show()

plt.bar('Car Model', 'Price (in USD)' ,data=bm )
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.grid(True)
plt.title("BMW")
plt.show()

plt.bar('Car Model', 'Price (in USD)', data=l  )
plt.title("Lamborghini")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.grid(True)
plt.show()


plt.bar('Car Model', 'Price (in USD)', data=m)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.title("McLaren")
plt.grid(True)
plt.show()


plt.bar('Car Model', 'Price (in USD)', data=k)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.title("Koenigsegg")
plt.grid(True)
plt.show()

plt.pie(car['Car Make'].value_counts(), labels=car['Car Make'].unique())
plt.show()
""" 

