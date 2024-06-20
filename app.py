from flask import Flask,render_template,request
import requests

app = Flask(__name__)

headers = {"Authorization": "Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query(payload):
   response=requests.post(API_URL,headers=headers,json=payload)
   return response.json()

@app.route('/', methods=['GET'])
def index():
   return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize():
   input_text=request.form["input_text"]
   minL= int(request.form["minL"])
   maxL= int(request.form["maxL"])
   output_text=query({"inputs":input_text,"parameters":{"min_length":minL,"max_length":maxL}})
   output_text_only = output_text[0]['summary_text']
   return render_template("index.html",summary_text=output_text_only,input=input_text)

if __name__ =='__main__':
   app.run(debug=False,host="0.0.0.0")
