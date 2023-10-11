from connect import *

def calculateprof_data():
    dbCursor.execute("SELECT AVG(productPrice - productCost) from products")
    average = dbCursor.fetchone()
    if average:
        averageACM = average[0]
        

    dbCursor.execute("SELECT productName, (productPrice - productCost) from products")
    productContribution = dbCursor.fetchall()

    profitability_products = []
    
    for products in productContribution:
        productName = products[0]
        individualProductCM = products[1]

        is_profitable = averageACM < individualProductCM
        profitability_products.append({'productName': productName, 'isProfitable': is_profitable})

    return profitability_products

def calculatepop_data():
    dbCursor.execute("SELECT productName, productSales FROM products")
    results = dbCursor.fetchall()

    popularity_products = []

    if results:
        for row in results:
            product_name = row[0]
            product_sales = row[1]

            total_sales = sum(r[1] for r in results) - product_sales
            total_products = len(results) - 1
            expected_popularity = (100 / total_products) * total_sales / 100

            is_popular = product_sales >= 0.7 * expected_popularity
            popularity_products.append({'productName': product_name, 'isPopular': is_popular})

    return popularity_products

def categorize_products():
    profitability_products = calculateprof_data()
    popularity_products = calculatepop_data()

    categorized_products = {}

    for product_profit in profitability_products:
        product_name = product_profit['productName']
        is_profitable = product_profit['isProfitable']

        is_popular = None
        for product_pop in popularity_products:
            if product_pop['productName'] == product_name:
                is_popular = product_pop['isPopular']
                break

        category = None
        if is_profitable and is_popular:
            category = "Star"
        elif is_profitable and not is_popular:
            category = "Plow horse"
        elif not is_profitable and is_popular:
            category = "Puzzle"
        else:
            category = "Dog"

        print(f"Product: {product_name}, Category: {category}")

if __name__ == "__main__":
    categorize_products()
