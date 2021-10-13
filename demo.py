from sentiment_classifier import PhoneSentimentClassifier, MoviesSentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)



print('init')
model_selected = False
model = None

def get_model(inp_type):
    if inp_type == 'phone_clf':
        print("Preparing classifier")
        start_time = time.time()
        classifier = PhoneSentimentClassifier()
        print("Classifier is ready")
        print(time.time() - start_time, "seconds")
        return classifier
    elif inp_type == 'movies_clf':
        print("Preparing classifier")
        start_time = time.time()
        classifier = MoviesSentimentClassifier()
        print("Classifier is ready")
        print(time.time() - start_time, "seconds")
        return classifier
    else:
        model_selected = False
        model = None



@app.route("/", methods=["POST", "GET"])
def index_page(text="", model_type = '', prediction_message=""):
    global model_selected
    global model
    
    if request.method == "POST":
        model_type = request.form["model_type"]
        model_selected = True
        model = get_model(model_type)
        print('model loaded')
        
        
    if model_selected:
        print(model_type)
        if text != '':
            prediction_message = model.get_prediction_message(text)
        else:
            prediction_message = 'neutral'
        if model_type == 'movies_clf':
            return render_template('movies_input_review.html', text=text, model_type=model_type, prediction_message=prediction_message)
        elif model_type == 'phone_clf':
            return render_template('phone_input_review.html', text=text, model_type=model_type, prediction_message=prediction_message)
        else:
            return render_template('index.html', text=text, prediction_message=prediction_message)

    
    return render_template('index.html', text=text, prediction_message=prediction_message)


@app.route("/phone_page", methods=["POST", "GET"])
def phone_page(text="", model_type = '', prediction_message=""):
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
        
        
    if model_selected:
        if text != '':
            prediction_message = model.get_prediction_message(text)
        else:
            prediction_message = 'neutral'
        return render_template('phone_input_review.html', text=text, model_type=model_type, prediction_message=prediction_message)

    
    return render_template('index.html', text=text, prediction_message=prediction_message)


@app.route("/movies_page", methods=["POST", "GET"])
def movies_page(text="", model_type = '', prediction_message=""):
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
        
        
    if model_selected:
        if text != '':
            prediction_message = model.get_prediction_message(text)
        else:
            prediction_message = 'neutral'
        return render_template('movies_input_review.html', text=text, model_type=model_type, prediction_message=prediction_message)

    
    return render_template('index.html', text=text, prediction_message=prediction_message)

if __name__ == "__main__":
    app.run()