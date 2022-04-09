from joblib import load # type: ignore

labels = [
    "Adult",
    "Business/Corporate",
    "Computers and Technology",
    "E-Commerce",
    "Education",
    "Food",
    "Forums",
    "Games",
    "Health and Fitness",
    "Law and Government",
    "News",
    "Photography",
    "Social Networking and Messaging",
    "Sports",
    "Streaming Services",
    "Travel",
]

model_name = "app/models/domain/comclas.joblib"


class ModelNotFoundError(Exception):
    pass


def predict(text: str) -> str:
    try:
        clf = load(model_name)
    except:
        raise ModelNotFoundError("Model not found")
    return labels[clf.predict([text])[0]] # type: ignore
