import csv
import json
from collections import defaultdict, Counter
from datetime import datetime
import re #para o regex

#1
# def calculate_sales(arquivo_csv, valor_filter):
#     total_sales_per_product = {}
#     diary_sales = {}
#     sales_above = []
#
#     with open(arquivo_csv, encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)
#
#         for data, product, quantity, price in reader:
#             quantity, price = int(quantity), float(price)
#             total_sale = quantity * price
#
#             total_sales_per_product[product] = total_sales_per_product.get(product, 0) + total_sale
#
#             diary_sales[data] = diary_sales.get(data, 0) + total_sale
#
#             if total_sale > valor_filter:
#                 sales_above.append((data, product, quantity, price, total_sale))
#
#     biggest_sales_day = max(diary_sales, key=diary_sales.get)
#
#     print("Total sales for each product: ")
#     for product, total in total_sales_per_product.items():
#         print(f"{product}: R$ {total:.2f}")
#
#     print(f"\nDay with highest sales: {biggest_sales_day}, with a total of R$ {diary_sales[biggest_sales_day]:.2f}")
#
#     print("\nSales above R$ 500:")
#     for data, product, quantity, price, total_sale in sales_above:
#         print(f"Date: {data}, Product: {product}, Quantity: {quantity}, Price: R$ {price:.2f}, Total Sale: R$ {total_sale:.2f}")
#
# calculate_sales('vendas.csv', 500)

#2

# import csv
# from collections import defaultdict, Counter
#
# def process_transaction(csv_file, prices):
#     total_per_client = defaultdict(int)
#     spent_per_client = defaultdict(float)
#     products_sold = Counter()
#
#     with open(csv_file, encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#
#         for row in reader:
#             cliente_id = row['cliente_id']
#             produto = row['produto']
#             quantidade = int(row['quantidade'])
#             total_per_client[cliente_id] += quantidade
#             products_sold[produto] += quantidade
#             spent_per_client[cliente_id] += quantidade * prices.get(produto, 0)
#
#     best_selling_products = products_sold.most_common(3)
#
#     print("Quantidade total comprada por cada cliente:")
#     for cliente, total in total_per_client.items():
#         print(f"Cliente {cliente}: {total} itens")
#
#     print("\nTrês produtos mais vendidos:")
#     for produto, total in best_selling_products:
#         print(f"{produto}: {total} unidades vendidas")
#
#     print("\nValor total gasto por cada cliente:")
#     for cliente, total_gasto in spent_per_client.items():
#         print(f"Cliente {cliente}: R$ {total_gasto:.2f}")
#
# prices = {
#     'Camiseta': 70.0,
#     'Calça': 120.0,
#     'Sapato': 150.0,
#     'Bolsa': 250.0,
#     'Relógio': 300.0
# }
#
# # Chamando a função com o nome do arquivo CSV e dicionário de preços
# process_transaction('transacoes.csv', prices)

#3

# import json
# from collections import defaultdict
#
# def process_employees(json_file, minimum_wage, new_json_file):
#     with open(json_file, 'r', encoding='utf-8') as file:
#         employees = json.load(file)
#
#     total_wage_per_departament = defaultdict(float)
#     counter_per_departament = defaultdict(int)
#
#     different_positions = set()
#
#     overpaid_employees = []
#
#     for employee in employees:
#         departament = employee['departamento']
#         salary = employee['salario']
#         position = employee['cargo']
#
#         total_wage_per_departament[departament] += salary
#         counter_per_departament[departament] += 1
#
#         different_positions.add(position)
#
#         if salary > minimum_wage:
#             overpaid_employees.append(employee)
#
#     average_wage_per_departament = {
#         departament: total_wage / counter_per_departament[departament]
#         for departament, total_wage in total_wage_per_departament.items()
#     }
#
#     with open(new_json_file, 'w', encoding='utf-8') as file:
#         json.dump(overpaid_employees, file, ensure_ascii=False, indent=4)
#
#     print("Salário médio por departamento:")
#     for departament, average_wage in average_wage_per_departament.items():
#         print(f"{departament}: R$ {average_wage:.2f}")
#
#     print("\nCargos distintos:")
#     for position in sorted(different_positions):
#         print(position)
#
# minimum_wage = 5000
# json_file = 'funcionarios.json'
# new_json_file = 'funcionarios_acima_salario.json'
#
# process_employees(json_file, minimum_wage, new_json_file)

#4

# def process_products(csv_file):
#     today = datetime.now().date()
#     products = []
#
#     with open(csv_file, 'r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             row['preco'] = float(row['preco'])
#             row['estoque'] = int(row['estoque'])
#             row['data_de_validade'] = datetime.strptime(row['data_de_validade'], '%Y-%m-%d').date()
#             products.append(row)
#
#     products = [product for product in products if product['data_de_validade'] >= today]
#
#     products_sorted_by_price = sorted(products, key=lambda x: x['preco'], reverse=True)
#
#     price_per_category = defaultdict(list)
#     for product in products:
#         price_per_category[product['categoria']].append(product['preco'])
#
#     avg_price_per_category = {category: sum(prices) / len(prices) for category, prices in price_per_category.items()}
#
#     print("Produtos ordenados pelo preço (ordem decrescente):")
#     for product in products_sorted_by_price:
#         print(f"{product['produto']}: R$ {product['preco']:.2f}")
#
#     print("\nMédia de preço por categoria:")
#     for category, avg_price in avg_price_per_category.items():
#         print(f"{category}: R$ {avg_price:.2f}")
#
# process_products('produtos.csv')

#5

# def process_comments(text_file, output_file):
#     count_excellent = 0
#     count_good = 0
#     count_bad = 0
#
#     emails = []
#     refund_or_problem_comments = []
#     # usando regex, sequencia de caracteres especiais para detectar padrões de texto, nesse caso e-mails
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     keywords = {
#         "excelente": "excellent",
#         "bom": "good",
#         "ruim": "bad"
#     }
#    #\b para marcar inicio e fim da palavra
#     with open(text_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             count_excellent += len(re.findall(r'\bexcelente\b', line, re.IGNORECASE))
#             count_good += len(re.findall(r'\bbom\b', line, re.IGNORECASE))
#             count_bad += len(re.findall(r'\bruim\b', line, re.IGNORECASE))
#
#             emails.extend(re.findall(email_pattern, line))
#
#             if re.search(r'\breembolso\b|\bproblema\b', line, re.IGNORECASE):
#                 refund_or_problem_comments.append(line.strip())
#
#     with open(output_file, 'w', encoding='utf-8') as output:
#         for comment in refund_or_problem_comments:
#             output.write(comment + '\n')
#
#     print(f"Palavra 'excelente' aparece {count_excellent} vezes.")
#     print(f"Palavra 'bom' aparece {count_good} vezes.")
#     print(f"Palavra 'ruim' aparece {count_bad} vezes.")
#     print("\nE-mails encontrados:")
#     for email in emails:
#         print(email)
#
# input_file = 'comentarios.txt'
# output_file = 'comentarios_reembolso_problema.txt'
#
# process_comments(input_file, output_file)

#6

# def process_access_data(csv_file):
#     total_time_per_day = defaultdict(int)
#     access_count_per_day = defaultdict(int)
#
#     with open(csv_file, encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#
#         for row in reader:
#             access_date = datetime.strptime(row['data_acesso'], "%Y-%m-%d")
#             time_spent = int(row['tempo_no_site'])
#
#             total_time_per_day[access_date] += time_spent
#             access_count_per_day[access_date] += 1
#
#     average_time_per_day = {
#         date: total_time / access_count_per_day[date]
#         for date, total_time in total_time_per_day.items()
#     }
#
#     most_accessed_day = max(access_count_per_day, key=access_count_per_day.get)
#     total_time_most_accessed_day = total_time_per_day[most_accessed_day]
#
#     print("Media de tempo gasto por dia:")
#     for date, avg_time in average_time_per_day.items():
#         print(f"{date.date()}: {avg_time:.2f} minutos")
#
#     print(
#         f"\nDia com mais acessos: {most_accessed_day.date()}, tempo total gasto: {total_time_most_accessed_day} minutos")
#
# process_access_data('acessos.csv')

#7
#
# def process_salary_data(employees_file, salaries_file):
#     employees_data = {}
#     total_salary_per_department = defaultdict(float)
#     count_per_department = defaultdict(int)
#
#     with open(employees_file, encoding="utf-8") as emp_file:
#         reader = csv.DictReader(emp_file)
#         for row in reader:
#             funcionario_id = int(row['funcionario_id'])
#             employees_data[funcionario_id] = {
#                 "nome": row['nome'],
#                 "departamento": row['departamento']
#             }
#
#     with open(salaries_file, encoding="utf-8") as sal_file:
#         reader = csv.DictReader(sal_file)
#         for row in reader:
#             funcionario_id = int(row['funcionario_id'])
#             salario = float(row['salario'])
#             bonus = float(row['bonus'])
#             salario_total = salario + bonus
#
#             if funcionario_id in employees_data:
#                 departamento = employees_data[funcionario_id]["departamento"]
#                 employees_data[funcionario_id]["salario_total"] = salario_total
#                 total_salary_per_department[departamento] += salario_total
#                 count_per_department[departamento] += 1
#
#     average_salary_per_department = {
#         department: total / count_per_department[department]
#         for department, total in total_salary_per_department.items()
#     }
#
#     print("Salário total por funcionário:")
#     for funcionario_id, data in employees_data.items():
#         print(f"{data['nome']} ({data['departamento']}): R$ {data['salario_total']:.2f}")
#
#     print("\nSalário médio total por departamento:")
#     for departamento, salario_medio in average_salary_per_department.items():
#         print(f"{departamento}: R$ {salario_medio:.2f}")
#
# process_salary_data('funcionarios.csv', 'salarios.csv')

#8
#
#acrescentei alunos de af, já que não havia um destino para os com nota >= 5 e <=7
#
# def process_student_data(json_file, approved_csv_file, failed_json_file, final_test_students_json_file):
#     with open(json_file, 'r', encoding='utf-8') as file:
#         students = json.load(file)
#
#     approved_students = []
#     failed_students = []
#     final_test_students = []
#
#     for student in students:
#         if student["nota"] > 7.0:
#             approved_students.append(student)
#         elif 5.0 <= student["nota"] <= 7.0:
#             final_test_students.append(student)
#         elif student["nota"] < 5.0:
#             failed_students.append(student)
#
#     with open(approved_csv_file, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=["nome", "nota", "turma"])
#         writer.writeheader()
#         writer.writerows(approved_students)
#
#     with open(failed_json_file, 'w', encoding='utf-8') as file:
#         json.dump(failed_students, file, ensure_ascii=False, indent=4)
#
#     with open(final_test_students_json_file, 'w', encoding='utf-8') as file:
#         json.dump(final_test_students, file, ensure_ascii=False, indent=4)
#
#     print(f"Total de alunos aprovados: {len(approved_students)}")
#     print(f"Total de alunos reprovados: {len(failed_students)}")
#     print(f"Alunos em prova final: {len(final_test_students)}")
#
# process_student_data('alunos.json', 'alunos_aprovados.csv', 'alunos_reprovados.json', 'alunos_final_test.json')


#9

def process_temperatures(csv_file):
    monthly_temperatures = defaultdict(lambda: defaultdict(list))

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = datetime.strptime(row['data'], '%Y-%m-%d')
            city = row['cidade']
            temperature = float(row['temperatura'])

            monthly_temperatures[city][date.strftime('%Y-%m')].append(temperature)

    average_temperatures = {}
    hottest_coldest_months = {}

    for city, months in monthly_temperatures.items():
        city_averages = {}
        hottest_month, coldest_month = '', ''
        max_temp, min_temp = float('-inf'), float('inf')

        for month, temps in months.items():
            avg_temp = sum(temps) / len(temps)
            city_averages[month] = avg_temp

            if avg_temp > max_temp:
                max_temp = avg_temp
                hottest_month = month
            if avg_temp < min_temp:
                min_temp = avg_temp
                coldest_month = month

        average_temperatures[city] = city_averages
        hottest_coldest_months[city] = {'Mais quente': hottest_month, 'Mais frio': coldest_month}

    print("Média de temperatura por mês para cada cidade:")
    for city, months in average_temperatures.items():
        print(f"\nCidade: {city}")
        for month, avg_temp in months.items():
            print(f"{month}: {avg_temp:.2f} °C")

    print("\nMês mais quente e mais frio para cada cidade:")
    for city, extremes in hottest_coldest_months.items():
        print(f"\nCidade: {city}")
        print(f"Mês mais quente: {extremes['Mais quente']}")
        print(f"Mês mais frio: {extremes['Mais frio']}")

process_temperatures('temperaturas.csv')



