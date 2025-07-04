from django import forms

class BudgetForm(forms.Form):
    monthly_income = forms.DecimalField(label="Monthly Income", min_value=0)
    rent = forms.DecimalField(label="Rent", min_value=0)
    groceries = forms.DecimalField(label="Groceries", min_value=0)
    utilities = forms.DecimalField(label="Utilities", min_value=0)
    savings_goal = forms.DecimalField(label="Savings Goal", min_value=0, required=False)
