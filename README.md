# GUARDA

- Versão do Python utilizada: 2.7
- Programa deve ser rodado em Distribuições/Sistemas baseados em Linux

------------------------------------------------------------------------------------------

## FUNCIONALIDADE
  O programa GUARDA tem como propósito garantir a autênticação de um conjunto de arquivos
 para uma determinada pasta utilizando calculo de HMAC.
   
------------------------------------------------------------------------------------------

### ESPECIFICAÇÕES

 - Função Hash Criptográfica utilizada: MD5
 - Todas as Hashs são salvas em um arquivo oculto na pasta do projeto nomeado _hashs_
 - Arquivo *Hashs* segue o modelo de armazenamento JSON

------------------------------------------------------------------------------------------

#### *Modo de uso:*

> Abra o Terminal (CTRL + ALT + T)

>> Navegue até a pasta que se encontra o arquivo Guarda.py

>>> A linha de comando segue o seguinte padrão: python2.7 Guarda.py *<opção>* *<diretório do projeto>*
>>> *Opções*:
>>> - "-i" Iniciar a guarda do diretório 
>>> - "-t" faz o rastreio (tracking) do diretório
>>> - "-x" desativa a guarda
