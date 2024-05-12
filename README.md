# Globo Esportes - e-Sports Scrapy

## Descrição
Este projeto tem como objetivo extrair notícias relacionadas ao meio de e-Sports do site Globo Esportes e subir essas notícias para o Google BigQuery.

## Passo a Passo

### Entendimento do Scrapy
Inicialmente, dediquei tempo para entender o funcionamento do framework Scrapy, que é uma ferramenta poderosa para extração de dados da web. 

### Coleta de Informações Básicas
Comecei coletando informações básicas, como o título de cada uma das notícias disponíveis no site. Isso me permitiu ter uma ideia do layout do site e dos elementos que precisaria extrair.

### Coleta de Links das Notícias
Em seguida, avancei para a coleta dos links de todas as notícias. Esses links seriam necessários para acessar cada página individualmente e extrair informações mais detalhadas, como o autor da matéria.

### Exploração de Múltiplas Páginas
Após coletar os links e todas as informações das notícias da primeira página, surgiu o desafio de encontrar um método para navegar por várias páginas e extrair as notícias de todas elas, garantindo que não ficássemos limitados apenas à página principal do site.

### Construção do DataFrame
Com todos os dados coletados de todas as páginas desejadas, adicionei tudo em um DataFrame do pandas. Isso facilitou a manipulação e organização dos dados antes de enviá-los para o Google BigQuery.

### Envio para o Google BigQuery
Por fim, o DataFrame contendo todas as notícias coletadas é carregado para o Google BigQuery, onde os dados ficam armazenados e disponíveis para análise e consulta. Além disso, o mesmo DataFrame é salvo localmente como um arquivo CSV com o nome gesports.csv.

