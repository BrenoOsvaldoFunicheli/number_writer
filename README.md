# number_writer

 
## Sections

* :scroll: [Padrões](#scroll) (optional)
* :blue_book: [Requisições](#blue_book)
* :postbox: [Testing e App](#postbox)

## :scroll: Padrões

Para esse projeto foram implementados alguns conceitos de programação e especificas do python

### Conceitos

* Versioning: Foi utilizado o sistemas de versionamento Git para manutenço de código multi-máquinas.

* POO e funcional programing: Foram implementados conceitos de classes concretas e métodos abstratos, bem como programação funcional.

* Módulos: O programa solução foi construído como um pacote python com diversos módulo e publicado no Pypi, permitindo extensões.


## :blue_book: Requisições


Escreva um código que leia um valor em reais e escreva o valor por extenso,

Ex: 1,00 => um real
1000,54 => mil reais e cinquenta e quatro centavos

O programa deverá receber o caminho de um arquivo txt de entrada, e o caminho de um arquivo txt de saída. O script irá ler o arquivo de entrada, onde cada linha do arquivo irá conter um valor em reais no formato XXXX,XX.  Para cada linha do arquivo de entrada, deverá ser escrita uma linha de saída no arquivo de saída com o valor original e o valor por extenso.



## :postbox: Testing e App

Automação de teste é o uso de software para controlar a execução do teste de software, a comparação dos resultados esperados com os resultados reais, a configuração das pré-condições de teste e outras funções de controle e relatório de teste.
Neste repositório eu forneço algumas tarefas para mostrar o conhecimento com testes.


Existem duas maneiras de construir e executar este aplicativo, primeiro executando com isolate app, segundo é baixando o pacote com pypi.

### Normal build

1. Get repository
2. Make the virtualenv
3. Run o virtualenv
4. Install all dependecies
5. Run test
6. Run app

```console

    git clone https://github.com/BrenoOsvaldoFunicheli/number_writer
    python3 -m venv .env
    source .env/bin/activate
    cd number_writer/
    pip install -r requirements.txt
    python pytest
    python number_writer -i input.txt -o output.txt -l pt

```


