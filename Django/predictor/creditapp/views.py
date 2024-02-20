# from django.shortcuts import render
# from django.http import HttpResponse
# from django import forms
# from django.views import View
# import pickle
# import pandas as pd

# # Load the pre-trained model
# with open('creditapp/model/model.pkl', 'rb') as f:
#     model = pickle.load(f)

# class CreditAppForm(forms.Form):
#     customer_id = forms.CharField(label='Customer ID')
#     month = forms.IntegerField(label='Month')
#     annual_income = forms.FloatField(label='Annual Income')
#     num_credit_cards = forms.FloatField(label='Number of Credit Cards')
#     interest_rate = forms.FloatField(label='Interest Rate')
#     due_date = forms.FloatField(label='Due Date')
#     num_inquiries = forms.FloatField(label='Number of Inquiries')
#     mix = forms.IntegerField(label='Credit Mix')
#     debt = forms.FloatField(label='Debt')
#     history_age = forms.FloatField(label='History Age')
#     invested_monthly = forms.FloatField(label='Invested Monthly')

# class HomeView(View):
#     def get(self, request):
#         form = CreditAppForm()
#         return render(request, 'home.html', {'form': form})

# class PredictResultView(View):
#     def post(self, request):
#         form = CreditAppForm(request.POST)
#         if form.is_valid():
#             user_input = pd.DataFrame(form.cleaned_data, index=[0])
#             # prediction = model.predict(user_input)
#             prediction = user_input
#             return render(request, 'result.html', {'prediction': prediction[0]})
#         # else:
#             # return render(request, 'home.html', {'form': form})
#             # return HttpResponse("Error")


from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd

model = pickle.load(open('creditapp/model/model.pkl','rb'))

def home(request):
    return render(request, 'home.html')

def predict_result(request):
    if request.method == 'POST':
        # Get user input from the form
        customer_id = request.POST['customer_id']
        month = int(request.POST['month'])
        annual_income = float(request.POST['annual income'])
        num_credit_card = float(request.POST['credit cards'])
        interest_rate = float(request.POST['interest rate'])
        due_date = float(request.POST['due date'])
        num_inquiries = float(request.POST['inquiries'])
        mix = int(request.POST['mix'])
        debt = float(request.POST['debt'])
        history_age = float(request.POST['history age'])
        invested_monthly = float(request.POST['invested monthly'])

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
        return render(request, 'result.html', {'prediction': prediction[0]})
    else:
        return render(request, 'home.html')