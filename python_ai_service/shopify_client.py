def run_shopify_query(store_id, query):
    # MOCK DATA (Interview friendly)
    if "inventory" in query:
        return {"daily_sales": 10}
    elif "orders" in query:
        return {"top_product": "T-Shirt", "units": 120}
    elif "customer" in query:
        return {"repeat_customers": 25}
    return {}
