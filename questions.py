import csv

def calculate_sales(arquivo_csv, valor_filter):
    total_sales_per_product = {}
    diary_sales = {}
    sales_above = []

    with open(arquivo_csv, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for data, product, quantity, price in reader:
            quantity, price = int(quantity), float(price)
            total_sale = quantity * price

            total_sales_per_product[product] = total_sales_per_product.get(product, 0) + total_sale

            diary_sales[data] = diary_sales.get(data, 0) + total_sale

            if total_sale > valor_filter:
                sales_above.append((data, product, quantity, price, total_sale))

    biggest_sales_day = max(diary_sales, key=diary_sales.get)

    print("Total sales for each product: ")
    for product, total in total_sales_per_product.items():
        print(f"{product}: R$ {total:.2f}")

    print(f"\nDay with highest sales: {biggest_sales_day}, with a total of R$ {diary_sales[biggest_sales_day]:.2f}")

    print("\nSales above R$ 500:")
    for data, product, quantity, price, total_sale in sales_above:
        print(f"Date: {data}, Product: {product}, Quantity: {quantity}, Price: R$ {price:.2f}, Total Sale: R$ {total_sale:.2f}")

calculate_sales('vendas.csv', 500)
