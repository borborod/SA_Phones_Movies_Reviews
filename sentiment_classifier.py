import joblib
import re



class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./sentiment_clf.pkl")
        self.classes_dict = {0: "Negative:(", 1: "Positive:)", -1: "prediction error"}

    def clean_text(self, inp_text):
        return re.sub(r"\s+", ' ', 
                      re.sub(r"[\d+]", '',
                             re.sub(r"[^\w\s]", '', inp_text.lower()).strip()
                             )
                     )

    def prepare_text(self, inp_text):
        return self.clean_text(inp_text)

    def predict_tonality(self, inp_text):
        text = self.prepare_text(inp_text)
        pred = self.model.predict([text])
        return pred[0]

    def get_prediction_message(self, text):
        prediction = self.predict_tonality(text)
        return self.classes_dict[prediction]