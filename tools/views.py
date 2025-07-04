from django.shortcuts import render
from .forms import BudgetForm

# Optional landing page view
def home(request):
    return render(request, "tools/home.html")

# Budget Planner Tool
def budget_planner(request):
    result = None
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            income = form.cleaned_data['monthly_income']
            rent = form.cleaned_data['rent']
            groceries = form.cleaned_data['groceries']
            utilities = form.cleaned_data['utilities']
            savings_goal = form.cleaned_data.get('savings_goal') or 0

            total_expenses = rent + groceries + utilities + savings_goal
            balance = income - total_expenses

            result = {
                "total_expenses": total_expenses,
                "balance": balance,
                "savings_goal": savings_goal
            }
    else:
        form = BudgetForm()

    return render(request, "tools/budget_form.html", {
        "form": form,
        "result": result
    })
