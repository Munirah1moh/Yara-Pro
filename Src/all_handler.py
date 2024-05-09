from yara_handler import *
from exiftool_handler import *



def ExportALLToCsv(metadata,dic,csv='all.csv'):

    try:

        if(len(dic)!=0):
            for d1, d2 in zip(metadata, dic):
                d1.update(d2)

            data_frame = pd.DataFrame.from_dict(metadata)

            data_frame.to_csv(csv)

    except Exception as e:
        print("Error at : ExportALLToCsv")
        print(e)
        print('Error pleace check yara-pro -h or yara-pro --help')


def ExportALLToHTML(metadata, dic, html='all.html'):
    try:
        for d1, d2 in zip(metadata, dic):
                d1.update(d2)
            
        data_frame = pd.DataFrame.from_dict(metadata)

        header = "Yara Pro REPORT"
  
        html_content = f'<h1>{header}</h1>\n' + data_frame.to_html(index=False)

        with open(html, 'w') as file:
            file.write(html_content)

    except Exception as e:
        print("Error at : ExportALLToHTML")
        print(e)
        print('Error please check yara-pro -h or yara-pro --help')