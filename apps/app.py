from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    name = request.form.get('name')
    interests = request.form.get('interests')
    education = request.form.get('education')

    # Perform career recommendation logic here
    # You may use machine learning models or other methods to make recommendations

    # Replace this with your recommendation logic
    recommendations = ['Career 1', 'Career 2', 'Career 3']

    return render_template('recommendation.html', name=name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
