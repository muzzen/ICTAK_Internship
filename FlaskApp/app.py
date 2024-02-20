from flask import Flask,render_template,request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model/model.pickle','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def predict_result():
    if request.method == 'POST':
        # Get user input from the form
        customer_id = request.form.get('customer_id')
        month = int(request.form.get('month'))
        annual_income = float(request.form.get('annual income'))
        num_credit_card = float(request.form.get('credit cards'))
        interest_rate = float(request.form.get('interest rate'))
        due_date = float(request.form.get('due date'))
        num_inquiries = float(request.form.get('inquiries'))
        mix = int(request.form.get('mix'))
        debt = float(request.form.get('debt'))
        history_age = float(request.form.get('history age'))
        invested_monthly = float(request.form.get('invested monthly'))

        # Create a DataFrame from the user input
        user_input = pd.DataFrame({
            'Customer_ID': [customer_id],
            'Month': [month],
            'Annual Income': [annual_income],
            'Num Credit Cards': [num_credit_card],
            'Interest Rate': [interest_rate],
            'Due Date': [due_date],
            'Num Inquiries': [num_inquiries],
            'Credit Mix': [mix],
            'Debt': [debt],
            'History Age': [history_age],
            'Invested Monthly': [invested_monthly]           
        })
    

        # Make predictions using the pre-trained model
        prediction = model.predict(user_input)

        # Display the prediction result
        return render_template('result.html', prediction = prediction[0])
    else:
        return render_template('home.html')
        
if __name__ == '__main__':
    app.run(port=8000)
