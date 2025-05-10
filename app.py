from flask import Flask, jsonify, request, render_template
import os
from flask_cors import CORS

app = Flask(__name__) # Flask construcror
CORS(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route("/submit", methods=["POST"])


def process():
    try:
        waist = int(request.form['waist'])
        tg = int(request.form['tg'])
        hdl = int(request.form['hdl'])
        bp = int(request.form['bp'])
        fpg = int(request.form['fpg'])
    except (TypeError, ValueError):
        return jsonify({"Error": "Invalid input data"}), 400

    if waist >= 94:
        count = 0
        if fpg >= 100:
            count += 1
        if hdl < 40:
            count += 1
        if tg >= 150:
            count += 1
        if bp >= 130:
            count += 1

        if count >= 2:
            result = "Metabolic Syndrome!"
        elif count == 1:
            result = "Cannot classify"
        else:
            result = "It's normal!"
    else:

        if fpg > 100 and tg > 150 and bp > 130:
            result = "Check your blood sugar, lipids, and blood pressure!"
        elif fpg > 100 and tg > 150:
            result = "Check your blood sugar and lipids!"
        elif fpg > 100 and bp > 130:
            result = "Check your blood sugar and blood pressure!"
        elif tg > 150 and bp > 130:
            result = "Check your lipids and blood pressure!"
        elif fpg > 100:
            result = "Check your blood sugar!"
        elif tg > 150:
            result = "Check your lipids!"
        elif bp > 130:
            result = "Check your blood pressure!"
        else:
            result = "It's normal!"





    return render_template('results.html', result_text=result)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
