from decimal import Decimal

def calculate_budget(data):
    income = data['monthly_income']
    rent = data['rent']
    groceries = data['groceries']
    utilities = data['utilities']
    savings_goal = data.get('savings_goal') or 0

    total_expenses = rent + groceries + utilities
    balance = income - total_expenses
    surplus_after_savings = balance - savings_goal

    status = "Healthy" if surplus_after_savings >= 0 else "Needs Adjustment"

    suggestions = []
    if rent > Decimal("0.4") * income:
        suggestions.append("🏠 Your rent is more than 40% of your income — consider downsizing.")
    if groceries > Decimal("0.3") * income:
        suggestions.append("🛒 Groceries are high — consider planning meals.")
    if balance < 0:
        suggestions.append("🔴 You're overspending — reduce your expenses.")
    elif surplus_after_savings < 0:
        suggestions.append("💡 You're not hitting your savings goal — try cutting back more.")

    return {
        "income": income,
        "total_expenses": total_expenses,
        "balance": balance,
        "savings_goal": savings_goal,
        "surplus_after_savings": surplus_after_savings,
        "status": status,
        "suggestions": suggestions
    }