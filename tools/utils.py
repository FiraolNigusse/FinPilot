from decimal import Decimal

def calculate_budget(data):
    income = data['monthly_income']
    rent = data['rent']
    groceries = data['groceries']
    utilities = data['utilities']
    savings_goal = data.get('savings_goal') or 0

    total_expenses = rent + groceries + utilities + savings_goal
    balance = income - total_expenses

    status = "Healthy" if balance >= savings_goal else "Needs Adjustment"

    suggestions = []
    if rent > Decimal("0.4") * income:
        suggestions.append("🏠 Your rent is more than 40% of your income — consider downsizing or renegotiating.")
    if groceries > Decimal("0.3") * income:
        suggestions.append("🛒 Groceries take a large chunk — plan meals or buy in bulk.")
    if balance < 0:
        suggestions.append("🔴 You're overspending — adjust your expenses.")
    if balance > Decimal("0.2") * income:
        suggestions.append("✅ Great! You have a good buffer — consider investing or saving more.")

    return {
        "income": income,
        "total_expenses": total_expenses,
        "balance": balance,
        "savings_goal": savings_goal,
        "status": status,
        "suggestions": suggestions
    }
