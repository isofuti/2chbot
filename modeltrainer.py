import pickle
import json
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def string_preparation(ogstr: str):
        
      newstr = ''

      for char in ogstr.lower():
            
          if char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
              newstr = newstr + char

      return newstr

with open('config.json', 'r', encoding='utf-8') as f:
  BOT_CONFIG = json.load(f)

X =[]
y = []

for category in BOT_CONFIG['categories'].keys():

  for example in BOT_CONFIG['categories'][category]['examples']:
    example = string_preparation(example)
    X.append(example)
    y.append(category)


print(len(X), len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y)

vectorizer = CountVectorizer(ngram_range=(2, 2), analyzer='char')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
print(len(vectorizer.get_feature_names()))

clf = LogisticRegression().fit(X_train_vectorized, y_train)

print(clf.score(X_train_vectorized, y_train))

print(clf.score(X_test_vectorized, y_test))

turple_objects = (clf, vectorizer)

pickle.dump(turple_objects, open('trainedmodel.pkl', 'wb'))
