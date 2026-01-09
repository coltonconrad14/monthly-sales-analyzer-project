# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key=None):
    """Calculates (and optionally prints) total sales within 30 days.

    - If `product_key` is one of "product_a", "product_b", or "product_c`, returns the
      total sales for that product over days 1..30 inclusive.
    - If `product_key` is None or "all", prints totals for all three products and
      returns a dict with the totals.
    """
    totals = {"product_a": 0, "product_b": 0, "product_c": 0}

    for row in data:
        day = row.get("day", 0)
        if 1 <= day <= 30:
            for key in totals:
                totals[key] += int(row.get(key, 0))

    if product_key is None or product_key == "all":
        print(f"Total sales within 30 days: product_a={totals['product_a']}, product_b={totals['product_b']}, product_c={totals['product_c']}")
        return totals

    if product_key in totals:
        return totals[product_key]

    raise ValueError(f"Unknown product_key: {product_key}")


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product.

    The average is computed over the available days in the range 1..30 found in `data`.
    """
    valid_products = {"product_a", "product_b", "product_c"}
    if product_key not in valid_products:
        raise ValueError(f"Unknown product_key: {product_key}")

    total = 0
    count = 0
    for row in data:
        day = row.get("day", 0)
        if 1 <= day <= 30:
            if product_key in row:
                total += int(row.get(product_key, 0))
                count += 1

    return (total / count) if count else 0.0


def best_selling_day(data):
    """Finds the day with the highest total sales.

    Returns the day (int) with the highest sum of product_a, product_b and product_c.
    Returns `None` if no valid data is present.
    """
    best_day = None
    best_total = None

    for row in data:
        day = row.get("day", 0)
        if 1 <= day <= 30:
            total = int(row.get("product_a", 0)) + int(row.get("product_b", 0)) + int(row.get("product_c", 0))
            if best_total is None or total > best_total:
                best_total = total
                best_day = day

    return best_day


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    valid_products = {"product_a", "product_b", "product_c"}
    if product_key not in valid_products:
        raise ValueError(f"Unknown product_key: {product_key}")

    count = 0
    for row in data:
        day = row.get("day", 0)
        if 1 <= day <= 30:
            if int(row.get(product_key, 0)) > threshold:
                count += 1

    return count


def top_product(data):
    """Determines which product had the highest total sales in 30 days.

    Returns the product key with the highest total (e.g. "product_a").
    If multiple products tie for the top, returns a list of product keys.
    Returns `None` if no valid data is present.
    """
    totals = {"product_a": 0, "product_b": 0, "product_c": 0}
    valid_day_found = False

    for row in data:
        day = row.get("day", 0)
        if 1 <= day <= 30:
            valid_day_found = True
            for key in totals:
                totals[key] += int(row.get(key, 0))

    if not valid_day_found:
        return None

    max_total = max(totals.values())
    top_products = [k for k, v in totals.items() if v == max_total]

    return top_products[0] if len(top_products) == 1 else top_products



# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
