import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


df=pd.read_csv("train.csv")
df.head()
df.info()
df.describe()
sns.countplot(x='Survived',data=df)
sns.barplot(x='Sex', y='Survived', data=df)
sns.barplot(x='Pclass', y='Survived', data=df)


df['Sex'] = df['Sex'].map({'male':0, 'female':1}).fillna(0) # Fill NaNs introduced by mapping with 0 (male)
df['Age'] = df['Age'].fillna(df['Age'].median())
# Safely get the mode for 'Embarked' or use 'S' as a fallback if mode is empty
embarked_mode = df['Embarked'].mode()
if not embarked_mode.empty:
    df['Embarked'] = df['Embarked'].fillna(embarked_mode[0])
else:
    df['Embarked'] = df['Embarked'].fillna('S') # Fallback if 'Embarked' is entirely NaN

df['Embarked'] = df['Embarked'].map({'S':0, 'C':1, 'Q':2}).fillna(0) # Fill NaNs introduced by mapping with 0 (S)

features = ['Pclass','Sex','Age','Fare','Embarked']
X = df[features]
y = df['Survived']

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)

models={
    "Logistic Regression":LogisticRegression(max_iter=200),
    "Random Forest":RandomForestClassifier(n_estimators=100),
    "Support Vector Machine":SVC(kernel='linear')
}
results={}
for name,model in models.items():
    model.fit(X_train.fillna(0),Y_train)
    Y_pred=model.predict(X_test.fillna(0))
    results[name]=accuracy_score(Y_test,Y_pred)

for name,acc in results.items():
  print(f"{name}:{acc:.2f}")

plt.bar(results.keys(), results.values())
plt.ylabel("Accuracy")
plt.title("Model Comparison")
plt.show()

best_model = RandomForestClassifier(n_estimators=100)
best_model.fit(X_train, Y_train)
y_pred = best_model.predict(X_test)

print(confusion_matrix(Y_test, y_pred))
print(classification_report(Y_test, y_pred))
