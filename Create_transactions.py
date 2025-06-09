import pandas as  pd

date = {
    'name': ['Ali ' , 'Kemal ' , 'Alex' ],
    'category': ['purchase' , 'subscription' , 'translation'],
    'summ': [950 , 1200, 2400 ,  ]
}
df = pd.DataFrame(date)
df.to_excel('transaction.xlsx', index=False)
print('the file was created successfully ''transactions.xlsx''')