import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib


# We already built our model
def spam_detection():
    data = pd.read_csv('./data/spam.csv')
    # print(data.head())
    # print(data.shape)
    data.drop_duplicates(inplace=True)
    # print(data.shape)
    # print(data.isnull().sum())
    data['Category'] = data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])
    # print(data.head())

    # Now we have to split the data to test and train data
    mess = data['Message']
    cat = data['Category']

    mess_train, mess_test, cat_train, cat_test = train_test_split(mess, cat, test_size=0.15)

    # This data is alfabet data, we have to convert it to decimal data
    cv = CountVectorizer(stop_words='english')  # common en words
    features = cv.fit_transform(mess_train)

    # Create and train the model
    model = MultinomialNB()
    model.fit(features, cat_train)

    # Test the model
    features_test = cv.transform(mess_test)
    # print(model.score(features_test, cat_test))  # 0.9854651162790697

    # Save the model and the CountVectorizer
    joblib.dump(model, 'data/spam_classifier_model.pkl')
    joblib.dump(cv, 'data/count_vectorizer.pkl')


def load_model(message):
    # Load the model and the CountVectorizer
    loaded_model = joblib.load(r'F:\datastractuer\spam detection\Spam\mail\data\spam_classifier_model.pkl')
    loaded_cv = joblib.load(r'F:\datastractuer\spam detection\Spam\mail\data\count_vectorizer.pkl')
    transformed_message = loaded_cv.transform([message])
    result = loaded_model.predict(transformed_message)
    return result[0]
# spam_detection()