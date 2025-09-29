from flask import Flask, request, jsonify
import pandas as pd
import Model_deployment as md
app = Flask(__name__)


@app.route('/predict_disease', methods=['POST'])
def predict():
    input_dict = request.get_json()
    data = pd.Series(input_dict)
    data = pd.DataFrame([data])
    print(data)
    prediction = md.do_prediction(data)
    return jsonify({'prediction': prediction[0]})


if __name__ =='__main__':
    app.run(debug=True)
    
        