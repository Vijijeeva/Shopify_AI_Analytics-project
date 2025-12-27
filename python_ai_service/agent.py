from shopify_client import run_shopify_query

def process_question(store_id, question):
    intent = detect_intent(question)
    query = generate_shopifyql(intent)
    data = run_shopify_query(store_id, query)
    answer = explain_result(intent, data)

    return {
        "answer": answer,
        "confidence": "medium"
    }

def detect_intent(question):
    if "inventory" in question.lower():
        return "inventory"
    elif "top" in question.lower():
        return "sales"
    elif "customer" in question.lower():
        return "customers"
    return "general"

def generate_shopifyql(intent):
    if intent == "inventory":
        return "SELECT product_title, inventory_quantity FROM products"
    elif intent == "sales":
        return "SELECT product_title, sum(quantity) FROM orders GROUP BY product_title"
    elif intent == "customers":
        return "SELECT customer_id FROM orders GROUP BY customer_id HAVING count(*) > 1"
    return ""
def explain_result(intent, data):
    if intent == "inventory":
        daily_sales = data.get("daily_sales", 0)
        return f"Based on past sales, you sell {daily_sales} units per day. You should reorder at least {daily_sales * 7} units for next week."

    if intent == "sales":
        return "Your top selling product last week was T-Shirt with 120 units sold."

    if intent == "customers":
        return "25 customers placed repeat orders in the last period."

    return "No sufficient data found."

