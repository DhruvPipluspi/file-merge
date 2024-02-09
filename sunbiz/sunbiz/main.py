import pandas as pd
import os



path = "F://file-merge//sunbiz//sunbiz//data"
dir_list = os.listdir(path)


main_df = pd.DataFrame()
for i in dir_list:

    df = pd.read_csv("data/"+str(i))
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
            judgment_debtor_list = judgment_debtor.split('\n\n')
        except:
            pass
        try:
            judgment_debtor_list = judgment_debtor.split('\n\n')
        except:
            pass
        i = 0

        while i < len(judgment_debtor_list):
            j = 0
            judgment_debtor_name = ''
            judgment_debtor_documentnumber = ''
            judgment_debtor_FEI_EIN = ''
            judgment_debtor_address = ''
            judgment_debtor_city = ''
            judgment_debtor_zip_city = ''
            judgment_debtor_zip = ''
            judgment_debtor_county = ''
            judgment_debtor_address_list = judgment_debtor_list[i].split('\n')
            while j < len(judgment_debtor_address_list):
                if j == 0:
                    judgment_debtor_name = judgment_debtor_address_list[j]
                elif j > 0 and "Document Number" in judgment_debtor_address_list[j]:
                    str_documentnumber = judgment_debtor_address_list[j]
                    judgment_debtor_documentnumber = str_documentnumber.split(":")[1]
                elif j > 0 and "FEI/EIN Number" in judgment_debtor_address_list[j]:
                    str_FEI_EIN = judgment_debtor_address_list[j]
                    judgment_debtor_FEI_EIN = str_FEI_EIN.split(":")[1]
                else:
                    if judgment_debtor_address == "":
                        judgment_debtor_address = judgment_debtor_address_list[j]
                    else:
                        judgment_debtor_address = judgment_debtor_address+"|"+judgment_debtor_address_list[j]
                        

                j+=1
            tem_str = ''
            temp = judgment_debtor_address.split("|")

            teee = temp[-1]
            judgment_debtor_city_pin = teee        
            temp.remove(temp[-1])
            judgment_debtor_address = ' '.join(temp)
            judgment_debtor_city = judgment_debtor_city_pin.split(",")[0]
            judgment_debtor_pin = (judgment_debtor_city_pin.split(",")[1]).strip()
            zip_list = judgment_debtor_pin.split(" ")
            if len(zip_list) == 1:
                judgment_debtor_zip_city = zip_list[0]
            elif len(zip_list) > 2 :
                judgment_debtor_zip_city = zip_list[0]
                judgment_debtor_county = zip_list[-1]
                judgment_debtor_zip = zip_list[1]
            else:
                judgment_debtor_zip_city = zip_list[0]
                judgment_debtor_zip = zip_list[-1]

            expiration_date = str(rows['expiration_date']).replace("-","/")
            i += 1
            # making data frame
            main_df = pd.concat([main_df, pd.DataFrame({
            'url': rows['url'],
            'search_key': rows['search_key'],
            'document_number': rows['document_number'],
            'status': rows['status'],
            'case_number': rows['case_number'],
            'name_of_court': rows['name_of_court'],
            'file_date': rows['file_date'],
            'date_of_entry': rows['date_of_entry'],
            'expiration_date': expiration_date,
            'amount_due': rows['amount_due'],
            'interest_rate': rows['interest_rate'],
            'debtor_name': judgment_debtor_name,
            'Debtor documentnumber': judgment_debtor_documentnumber,
            'Debtor FEI_EIN': judgment_debtor_FEI_EIN,
            'Debtor address': judgment_debtor_address,
            'Debtor city': judgment_debtor_city,
            'Debtor Zip City': judgment_debtor_zip_city,
            'Debtor zip Code': judgment_debtor_zip,
            'Debtor Zip County': judgment_debtor_county,
            'original_document': rows['original_document'],
            'scraped': rows['scraped'],
            'amount_remaining': rows['amount_remaining']
            }, index=[0])], ignore_index=True)
        
main_df.reset_index(drop=False, inplace=True)
main_df['index'] += 1


main_df.to_csv('main_df.csv', index=False)

