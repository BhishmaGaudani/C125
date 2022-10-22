from flask import Flask,jsonify,request
from Classifier import get_prediction

app=Flask(__name__)
@app.route("/predict-digit",methods=["POST"])
def predictData():
    img=request.files.get("digit3.jpeg")
    prediction=get_prediction(img)
    return jsonify({
        "prediction":prediction
    }),200

if __name__=="__main__":
    app.run(debug=True)
