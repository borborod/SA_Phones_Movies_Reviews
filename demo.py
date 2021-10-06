from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)



print('init')
model_selected = False
model = None

def get_model(inp_type):
    if inp_type == 'clf':
        print("Preparing classifier")
        start_time = time.time()
        classifier = SentimentClassifier()
        print("Classifier is ready")
        print(time.time() - start_time, "seconds")
        return classifier



@app.route("/", methods=["POST", "GET"])
def index_page(text="", model_type = '', prediction_message=""):
    global model_selected
    global model
    
    if request.method == "POST":
        if model_selected: 
            text = request.form["text"]
            logfile = open("ydf_demo_logs.txt", "a", "utf-8")
            print(text)
            logfile.write("<response>" + '\n')
            logfile.write(text + '\n')
            prediction_message = model.get_prediction_message(text)
            print(prediction_message)
            logfile.write(prediction_message + '\n')
            logfile.write("</response>" + '\n')
            logfile.close()
        else:
            model_type = request.form["model_type"]
            model_selected = True
            print(model_type)
            model = get_model(model_type)
            print('model loaded')
        
        
    if model_selected:
        if text != '':
            prediction_message = model.get_prediction_message(text)
        else:
            prediction_message = 'neutral'
        return render_template('input_review.html', text=text, model_type=model_type, prediction_message=prediction_message)
    
    return render_template('index.html', text=text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run()