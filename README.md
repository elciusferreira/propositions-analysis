# propositions-analysis
Análise das proposições feitas entre 1998 e 2016 que estão disponíveis como dados abertos no site da Câmara dos Deputados. Dados dos anos de 2017 e 2018 ainda não estão disponíveis.

Site: https://dadosabertos.camara.leg.br/swagger/api.html

Nele é possível encontrar arquivos no formato json com informações referentes às proposições feitas entre os anos de:
* 1998 e 2002
* 2002 e 2006
* 2006 e 2010
* 2010 e 2014
* 2014 e 2018

Foi feito o download dos 5 arquivos que posteriormente foram transformados em outros 5 no formato csv por um script implementado em python que realiza o parsing.

Uma análise individual foi feita para cada um dos 5 arquivos e, por fim, todos os csv's foram unidos em um único, para que fosse realizada uma análise gráfica geral, ou seja, de 1998 até 2018.
