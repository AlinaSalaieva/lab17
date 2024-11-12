import pandas as pd

data = pd.read_csv('sales_data.csv')

new_sales = {
    'Місяць': 'Березень',
    'Фірма1': int(input('Введіть кількість проданих автомобілів фірмою 1 за 3 місяць: ')),
    'Фірма2': int(input('Введіть кількість проданих автомобілів фірмою 2 за 3 місяць: ')),
    'Фірма3': int(input('Введіть кількість проданих автомобілів фірмою 3 за 3 місяць: ')),
    'Фірма4': int(input('Введіть кількість проданих автомобілів фірмою 4 за 3 місяць: '))
}

new_sales_df = pd.DataFrame([new_sales])
data = pd.concat([data, new_sales_df], ignore_index=True)

data.to_csv('updated_sales_data.csv', index=False)

print('Дані успішно збережено у файл updated_sales_data.csv')
