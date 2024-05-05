from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    main_data = {
        'Город': 'Чебоксары',
        'Район': 'Московский',
        'Компания': 'Iserv'
    }
    context = {
        'name': 'Артём',
        'age': '17',
        'spes': 'Пчеловод'

    }
    return render_template('index.html', main_data=main_data, **context)

@app.route("/contacts/")
def contacts():
    developer_name = 'Ilon_Mask'
    return render_template('contacts.html', name=developer_name)

@app.route("/results/")
def results():
    data = ['phyton', 'js', 'G0', 'c#', 'C++', 'lua', 'React', 'SQL', 'Postgesql']
    return render_template('results.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)