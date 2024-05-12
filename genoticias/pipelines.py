# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import pandas_gbq

class GenoticiasPipeline:
    dicio = []

    # Este método é chamado quando a spider é aberta.
    # https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    def open_spider(self, spider):


        self.dicio_lista = []

    # Este método é chamado para processar cada item coletado pela spider
    def process_item(self, item, spider):
        print('Esses são os itens', item)
        # Cria um dicionário com os dados do item
        dicio = {
                'autor': item['autor'],
                'titulo': item['titulo'],
                'subtitulo': item['subtitulo'],
                'link': item['link'],
                'publicacao': item['publicacao'],
            }

        self.dicio_lista.append(dicio)

        print('dicio_lista: ', len(self.dicio_lista))


        return item

    # Este método é chamado quando a spider é fechada
    def close_spider(self, spider):
        # Converte a lista de dicionários em um DataFrame pandas
        df = pd.DataFrame(columns=['autor', 'titulo', 'subtitulo', 'link', 'publicacao'])
        df = pd.DataFrame(self.dicio_lista)
        print('dataframe: ', df.head(5))

        # Configuração do BigQuery
        project_id = 'noticias-scrapy'
        table_id = 'gesports.noticias-gesports'
        key_path = "C:/Users/muril/OneDrive/Documentos/prog/gesports_key.json"
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        # Carrega o DataFrame para o BigQuery
        pandas_gbq.to_gbq(df, table_id, project_id, if_exists='replace', credentials=credentials)



