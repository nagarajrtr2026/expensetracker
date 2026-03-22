from storage.file_handler import load_data, save_data
from services.expense_service import add_expense, delete_expense
from services.analytics_service import *
from utils.generator import generate_fake_data
from visualization.charts import show_category_chart

def main():
    data = load_data()

    while True:
        print("\n1.Add 2.Delete 3.Total 4.Monthly 5.Category 6.Generate 7.Chart 8.Exit")
        ch = input("Choice: ")

        if ch == '1':
            add_expense(data)
            save_data(data)

        elif ch == '2':
            delete_expense(data)
            save_data(data)

        elif ch == '3':
            print("Total:", total(data))

        elif ch == '4':
            print(monthly_summary(data))

        elif ch == '5':
            print(category_summary(data))

        elif ch == '6':
            data.extend(generate_fake_data())
            save_data(data)
            print("Fake data added!")

        elif ch == '7':
            summary = category_summary(data)
            show_category_chart(summary)

        elif ch == '8':
            break

if __name__ == "__main__":
    main()