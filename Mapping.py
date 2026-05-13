import pandas as pd
from List import ValidListcol
from Loader import loader

def mapping(df,validlist):
      
    ValidList=validlist
    Finallist=[]
    Datalist=df.columns.to_list()
    

    df3=df
    df3 = df3.rename(columns={v: k for k, v in ValidList.items()})
      
    for key, values in ValidList.items():
       
       for valueslist in Datalist:

                if key.lower()==valueslist.lower():
                      Finallist.append(key)
                elif values.lower()==valueslist.lower():
                      Finallist.append(valueslist)


    df1=pd.Series(Finallist,name='Valid_col')

    
    for key2,Values2 in ValidList.items():

        df1=df1.str.replace(Values2,key2)

    Listpass=list(df1)
    df4=df3[Listpass]

    lst = df4.columns.to_list()

    max_len = max(len(Datalist), len(Finallist), len(lst))

# Equal length banane ke liye blanks add karo
    Datalist.extend([''] * (max_len - len(Datalist)))
    Finallist.extend([''] * (max_len - len(Finallist)))
    lst.extend([''] * (max_len - len(lst)))

    compare_table = pd.DataFrame({
        'Original Columns': Datalist,
        'Matched Columns': Finallist,
        'Final DF Columns': lst
    })

    print(compare_table)
    
    UserPermission=input("\nPlease Check Data Frame Columns Matched and Press 'y' to Process : ")
    if UserPermission=='y':
        print("\nProcess Plz Wait......")
         
        return df4
    else:
         print("\nProgram Exit !")
         exit()


ValidList= ValidListcol
df=loader()


DataFrame=mapping(df=df,validlist=ValidList) 
""" print(DataFrame) """


      




