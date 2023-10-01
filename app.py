import streamlit as st
import pickle
import sklearn
import numpy
import datetime as dt

filename1 = 'logistic_model.sav'
filename2 = 'svm_model.sav'
filename3 = 'naive_bayes_model.sav'
logistic_model = pickle.load(open(filename1, 'rb'))
random_forest_model = pickle.load(open(filename3, 'rb'))
naive_bayes_model = pickle.load(open(filename2, 'rb'))

# sidebar image
st.sidebar.image('personal-loan-3.jpg')
# sidebar title
st.sidebar.title("Loan Approval Prediction")
# radio buttons for selecting model type
selected = st.sidebar.radio(
    "Select an algorithm :",
    ("Logistic Regression", "Support Vector Machine", "Naive Bayes Classifier"),
)

# streamlit run app.py
# ctrl+c in terminal to kill the process

# if logistic regression is selected
if selected == 'Logistic Regression':
    # title for the page
    st.title("Logistic Regression")

    # text input
    user_name = st.text_input("Enter your name")
    # date input
    st.date_input("Enter your age", min_value=dt.date(1947,12,31), max_value=dt.date.today())
    # number input
    no_of_dependents = st.number_input("Enter the number of dependencies", min_value=0, step=1)

    # selection box input
    education = st.selectbox('Select education level', ('Graduate', 'Not Graduate'))
    if education == 'Graduate':
        education = 1
    else:
        education = 0

    # selection box input
    self_employed = st.radio('Self employed?', ('No', 'Yes'))
    if self_employed == 'Yes':
        self_employed = 1
    else:
        self_employed = 0

    # number input
    income_annum = st.number_input("Enter your annual income", step=10000)
    # number input
    loan_amount = st.number_input("Enter your expected loan amount", step=10000)
    # number input
    loan_term = st.number_input("In how much time your want to repay your loan", min_value=0, step=1)
    # number input
    cibil_score = st.number_input("Enter your cibil score", min_value=0, step=1)
    # number input
    residential_assets_value = st.number_input("Enter your residential assets value", min_value=0, step=10000)
    # number input
    commercial_assets_value = st.number_input("Enter your commercial assets value", min_value=0, step=10000)
    # number input
    luxury_assets_value = st.number_input("Enter your luxury assets value", min_value=0, step=10000)
    # number input
    bank_asset_value = st.number_input("Enter your bank assets value", min_value=0, step=10000)

    loan_approval_result = ''

    # button to predict the values
    # if condition is used to check weather the streamlit button is clicked or not
    if st.button("Loan approval"):
        loan_predict = logistic_model.predict([[no_of_dependents, int(education), int(self_employed), income_annum,
                                                loan_amount, loan_term, cibil_score, residential_assets_value,
                                                commercial_assets_value, luxury_assets_value, bank_asset_value]])

        if loan_predict[0] == 1:
            loan_approval_result = 'Congratulations your loan can be approved!'


        else:
            loan_approval_result = 'Sorry your loan cannot be approved.'

    # show the result
    st.success(loan_approval_result)


# if random forest is selected
if selected == 'Support Vector Machine':
    # title for the page
    st.title("Support Vector Machine")

    # text input
    st.text_input("Enter your name")
    # date input
    st.date_input("Enter your age", min_value=dt.date(1947,12,31), max_value=dt.date.today())
    # number input
    no_of_dependents = st.number_input("Enter the number of dependencies", min_value=0, step=1)

    # selection box input
    education = st.selectbox('Select education level', ('Graduate', 'Not Graduate'))
    if education == 'Graduate':
        education = 1
    else:
        education = 0

    # selection box input
    self_employed = st.radio('Self employed?', ('No', 'Yes'))
    if self_employed == 'Yes':
        self_employed = 1
    else:
        self_employed = 0

    # number input
    income_annum = st.number_input("Enter your annual income", step=10000)
    # number input
    loan_amount = st.number_input("Enter your expected loan amount", step=10000)
    # number input
    loan_term = st.number_input("In how much time your want to repay your loan", min_value=0, step=1)
    # number input
    cibil_score = st.number_input("Enter your cibil score", min_value=0, step=1)
    # number input
    residential_assets_value = st.number_input("Enter your residential assets value", min_value=0, step=10000)
    # number input
    commercial_assets_value = st.number_input("Enter your commercial assets value", min_value=0, step=10000)
    # number input
    luxury_assets_value = st.number_input("Enter your luxury assets value", min_value=0, step=10000)
    # number input
    bank_asset_value = st.number_input("Enter your bank assets value", min_value=0, step=10000)

    loan_approval_result = ''

    # button to predict the values
    # if condition is used to check weather the streamlit button is clicked or not
    if st.button("Loan approval"):
        loan_predict = random_forest_model.predict([[no_of_dependents, int(education), int(self_employed), income_annum,
                                                    loan_amount, loan_term, cibil_score, residential_assets_value,
                                                    commercial_assets_value, luxury_assets_value, bank_asset_value]])

        if loan_predict[0] == 1:
            loan_approval_result = 'Congratulations your loan can be approved!'


        else:
            loan_approval_result = 'Sorry your loan cannot be approved.'

    # show the result
    st.success(loan_approval_result)

# if naive bayes is selected
if selected == 'Naive Bayes Classifier':
    # title for the page
    st.title("Naive Bayes Classifier")

    # text input
    st.text_input("Enter your name")
    # date input
    st.date_input("Enter your age", min_value=dt.date(1947,12,31), max_value=dt.date.today())
    # number input
    no_of_dependents = st.number_input("Enter the number of dependencies", min_value=0, step=1)

    # selection box input
    education = st.selectbox('Select education level', ('Graduate', 'Not Graduate'))
    if education == 'Graduate':
        education = 1
    else:
        education = 0

    # selection box input
    self_employed = st.radio('Self employed?', ('No', 'Yes'))
    if self_employed == 'Yes':
        self_employed = 1
    else:
        self_employed = 0

    # number input
    income_annum = st.number_input("Enter your annual income", step=10000)
    # number input
    loan_amount = st.number_input("Enter your expected loan amount", step=10000)
    # number input
    loan_term = st.number_input("In how much time your want to repay your loan", min_value=0, step=1)
    # number input
    cibil_score = st.number_input("Enter your cibil score", min_value=0, step=1)
    # number input
    residential_assets_value = st.number_input("Enter your residential assets value", min_value=0, step=10000)
    # number input
    commercial_assets_value = st.number_input("Enter your commercial assets value", min_value=0, step=10000)
    # number input
    luxury_assets_value = st.number_input("Enter your luxury assets value", min_value=0, step=10000)
    # number input
    bank_asset_value = st.number_input("Enter your bank assets value", min_value=0, step=10000)

    loan_approval_result = ''
    # button to predict the values
    # if condition is used to check weather the streamlit button is clicked or not
    if st.button("Check Loan Status"):
        loan_predict = naive_bayes_model.predict([[no_of_dependents, int(education), int(self_employed), income_annum,
                                                    loan_amount, loan_term, cibil_score, residential_assets_value,
                                                    commercial_assets_value, luxury_assets_value, bank_asset_value]])

        if loan_predict[0] == 1:
            loan_approval_result = 'Congratulations your loan can be approved!'


        else:
            loan_approval_result = 'Sorry your loan cannot be approved.'

    # show the result
    st.success(loan_approval_result)