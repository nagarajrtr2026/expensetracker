from collections import defaultdict
from datetime import datetime

def total(data):
    return sum(d['amount'] for d in data)

def monthly_summary(data):
    summary = {}

    for d in data:
        month = d['date'][:7]  # YYYY-MM
        summary[month] = summary.get(month, 0) + d['amount']

    return summary

def category_summary(data):
    summary = {}

    for d in data:
        cat = d['category']
        summary[cat] = summary.get(cat, 0) + d['amount']

    return summary

def generate_monthly_expense_summary(data):
    """
    Generate a comprehensive monthly expense summary with detailed breakdowns.
    
    Args:
        data: List of expense dictionaries with 'category', 'amount', and 'date' keys
        
    Returns:
        Dictionary containing detailed monthly summaries with:
        - total: Total expenses for the month
        - count: Number of transactions
        - by_category: Breakdown of expenses by category
        - average_daily: Average daily expense
        - highest_expense: Highest single expense amount
        - lowest_expense: Lowest single expense amount
    """
    monthly_data = defaultdict(lambda: {
        'total': 0,
        'count': 0,
        'by_category': defaultdict(float),
        'expenses': []
    })
    
    # Group expenses by month
    for expense in data:
        month = expense['date'][:7]  # YYYY-MM format
        monthly_data[month]['total'] += expense['amount']
        monthly_data[month]['count'] += 1
        monthly_data[month]['by_category'][expense['category']] += expense['amount']
        monthly_data[month]['expenses'].append(expense['amount'])
    
    # Build final summary with additional metrics
    summary = {}
    for month in sorted(monthly_data.keys()):
        data_for_month = monthly_data[month]
        expenses_list = data_for_month['expenses']
        
        # Calculate days in month for average
        year, month_num = map(int, month.split('-'))
        if month_num == 12:
            next_month = f"{year + 1}-01-01"
        else:
            next_month = f"{year}-{month_num + 1:02d}-01"
        
        summary[month] = {
            'total': round(data_for_month['total'], 2),
            'count': data_for_month['count'],
            'by_category': dict(data_for_month['by_category']),
            'average_daily': round(data_for_month['total'] / 30, 2),  # Approximate 30 days
            'highest_expense': round(max(expenses_list), 2) if expenses_list else 0,
            'lowest_expense': round(min(expenses_list), 2) if expenses_list else 0,
        }
    
    return summary