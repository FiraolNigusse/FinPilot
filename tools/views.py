from django.shortcuts import render
from .forms import BudgetForm
from .utils import calculate_budget  # only if using utils.py
from django.contrib import messages
from datetime import datetime


def home(request):
    return render(request, "tools/home.html")  # basic template for now

def budget_planner(request):
    result = None
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            result = calculate_budget(form.cleaned_data)
            messages.success(request, "✅ Budget calculated successfully!")
        else:
            messages.error(request, "❌ Please correct the errors in the form.")    
    else:
        form = BudgetForm()

    return render(request, "tools/budget_result.html", {
        "form": form,
        "result": result,
        "now": datetime.now()
    })
