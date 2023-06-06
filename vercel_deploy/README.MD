# Exemplo de aplicação contendo tecnologia de templates do Jinja, arquivos externos CSS e imagens. 

## Autor: Fabrício Galende M. de Carvalho, PhD

Para executar o sistema:

1. Clonar o repositório
2. Criar o ambiente virtual:
```console
python -m virtualenv env
```
3. Ativar o ambiente virtual (no windows o arquivo é o .bat):
```console
env/Scripts/activate.bat
```
4. Instalar as dependências:
```console
pip install -r requirements.txt
```
5. Executar a aplicação (na pasta api/)
```console
python app.py
```



## Instruções para a implantação no Vercel

1. Instalar o node e seu gerenciador de pacotes, ou seja, o npm 
1. Instalar o vercel através do comando: 
    ```console 
    npm install -g vercel 
    ```
1. Considerando que você já criou uma conta no Vercel, e que
 está logado, utilize o comando seguinte no mesmo nível do arquivo vercel.json
    ```console 
    vercel
    ```
1. Defina um nome para a sua aplicação e utilize todas as demais opções de acordo com o padrão sugerido. 
1. Verifique se o link disponibilizado ao final do processo de upload/build está acessível, caso não esteja, execute o comando 
    ```console 
    vercel --prod 
    ```