from joblib import load

clf = load('app/models/domain/comclas.joblib')
labels = [
    'Adult',
    'Business/Corporate',
    'Computers and Technology',
    'E-Commerce',
    'Education',
    'Food',
    'Forums',
    'Games',
    'Health and Fitness',
    'Law and Government',
    'News',
    'Photography',
    'Social Networking and Messaging',
    'Sports',
    'Streaming Services',
    'Travel'
]

def predict(text:str) -> str:
    return labels[clf.predict([text])[0]]


