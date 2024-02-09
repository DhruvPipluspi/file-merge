import pandas as pd

df = pd.read_csv("data/debtors-from-searchkey-a-1-to-500-of-40880.csv")

df.rename(
    columns={
    "Name  And  Address of  Judgment  Creditor ( Plaintiff)":"judgment_crediter",
    "Name  And  Address of  Judgment  Debtor(s) ( Defendant(s))":"judgment_debtor",
    "Url":"url",
    "Search Key":"search_key",
    "Document  Number":"document_number",
    "Status":"status",
    "Case  Number":"case_number",
    "Name of  Court":"name_of_court",
    "File  Date":"file_date",
    "Date of  Entry":"date_of_entry",
    "Expiration  Date":"expiration_date",
    "Amount  Due":"amount_due",
    "Interest  Rate":"interest_rate",
    "Scraped":"scraped",
    "Original  Document":"original_document",
    "Amount  Remaining":"amount_remaining"
    },inplace=True)

pd.set_option('display.max_columns', None)
for index,rows in df.iterrows():
    url = rows['url']
    search_key = rows['search_key']
    document_number = rows['document_number']
    status = rows['status']
    case_number = rows['case_number']
    name_of_court = rows['name_of_court']
    file_date = rows['file_date']
    date_of_entry = rows['date_of_entry']
    expiration_date = rows['expiration_date']
    amount_due = rows['amount_due']
    interest_rate = rows['interest_rate']
    scraped = rows['scraped']
    original_document = rows['original_document']
    amount_remaining = rows['amount_remaining']
    judgment_crediter = rows['judgment_crediter']
    judgment_debtor = rows['judgment_debtor']
    try:
        judgment_crediter_list = judgment_crediter.split('\n')
    except:
        pass
    j = 0

    creditor_name = ''
    creditor_address = ''
    creditor_city = ''
    creditor_zip_city = ''
    creditor_zip = ''
    creditor_county = ''
    while j < len(judgment_crediter_list):
        if j == 0:
            creditor_name = judgment_crediter_list[j]
            print(creditor_name)
        else:
            if creditor_address == "":
                creditor_address = judgment_crediter_list[j]
            else:
                creditor_address = creditor_address+"|"+judgment_crediter_list[j]
                print(creditor_address)
        j+=1
        

