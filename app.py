from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/length', methods=['GET', 'POST'])
def length():
    units = {
        'millimeter': 0.1,
        'centimeter': 1,
        'meter': 100,
        'kilometer': 100000,
        'inch': 2.54,
        'foot': 30.48,
        'yard': 91.44,
        'mile': 160934
    }

    result = None
    value = from_unit = to_unit = ""

    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = value * units[from_unit] / units[to_unit]

    return render_template("length.html", result=result, value=value, from_unit=from_unit, to_unit=to_unit, units=units)

if __name__ == '__main__':
    print("Flask is working")
    app.run(debug=True)

