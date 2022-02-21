[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6317248&assignment_repo_type=AssignmentRepo)
# Atividade: Blocos (`02-blocks`)

Esta atividade tem como objetivo implementar o modelo de dados responsável por representar um bloco em nosso blockchain, além de implementar métodos responsáveis pela criação destes blocos.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas deve ser realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize a IDE de sua preferência (sugestão: Visual Studio Code).

As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instruções de submissão

Submissão deve ser feita a partir do GitHub Classroom até às 23:59 do dia 14/11/2021. Basta realizar o *commit* do seu arquivo `blockchain.py` no repositório privado criado para você a partir do link disponibilizado (associe sua conta GitHub ao seu nome na plataforma). Qualquer dúvida nesta etapa consulte o professor no Discord. **Atenção!** Não mexer/editar o arquivo `test_github_classroom.py`.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários. Todos os *boilerplates* são compatíveis com o Python 3+.

## Descrição

A estrutura/objeto/dicionário para representar um bloco deve seguir o seguinte modelo (atente aos nomes dos atributos e aos tipos de dados):

```python
{
    'index': 2, 
    'timestamp': 1506057125,
    'nonce': 324984,
    'merkleRoot': "13c8bbf1dde38d5f86bfc48a5c027df0d8eb19c8a647de49976755e1b35b31ca",
    'previousHash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
    'transactions': [] # Por enquanto usar lista vazia. 
}
```

Onde:

- `index`: índice do bloco, que representa a profundidade do bloco no blockchain (o bloco genesis tem `index` 0);
- `timestamp` : data (formato unix, somente segundos) de criação do novo bloco;
- `nonce` : por enquanto pode deixar esse atributo com valor 0;
- `merkleRoot` : por enquanto pode deixar esse atributo com valor 0x0;
- `previousHash` : *hash* do cabeçalho do bloco anterior. O cabeçalho é formado pelos campos `index`, `timestamp`, `nonce`, `merkleRoot` e `previousHash`. Calcule o *hash* do bloco a partir do dicionário que representa a estrutura, lembrando de excluir o atributo `transactions`, que não faz parte do cabeçalho;
- `transactions` : lista de transações incluídas no bloco; por enquanto pode deixar como uma lista vazia, não é necessário modelar a estrutura da transação neste momento.

A assinatura do método já está presente na classe `Blockchain`:

```python
def createBlock()
```

Implemente também o método `createGenesisBlock()`, responsável por criar o bloco Genêsis, invocando o método `createBlock()` previamente implementado:	

```python	
def createGenesisBlock()
```

Implemente também um método estático auxiliar para gerar o identificador (ID) de um bloco passado como parâmetro. Lembre que o ID de um bloco é a _hash_ (no nosso caso com a função SHA256) do **cabeçalho** de um bloco. Na nossa implementação, fazem parte do cabeçalho de um bloco os campos: `index`, `timestamp`, `nonce`, `merkleRoot` e `previousHash`. Dado essas informações, implemente o método estático `getBlockID(block)`:

```python
def getBlockID(block)
```

Note que o construtor já foi definido, assim como alguns atributos da classe `Blockchain`:	

- `chain` : uma lista de blocos, representando o blockchain; os blocos devem ser armazenados nessa lista de maneira ordenada. Por enquanto podemos incluir todo bloco criado, mesmo que não validado/minerado;
- `memPool` : o *memory pool*, responsável por armazenar, temporariamente, transações que ainda não foram incluídas em um bloco; não precisaremos utilizar esse atributo ainda.

Por fim, implemente o método `printChain()`, responsável por imprimir no terminal uma saída que represente o estado atual do seu blockchain, ressaltando os atributos de cada bloco. Um exemplo de *output* pode ser visto abaixo, mas sinta-se a vontade para implementar da maneira que desejar, desde que seja visualmente interessante:

```	
 __________________________________________________________________	
| 8e853d40b1931e0272ad33fae0f3854d9914aa6696653f01fa7a05584ac250dc |                	
 ------------------------------------------------------------------                	
| Índice:         Timestamp:              Nonce:                   |	
| 3               1566323766              0                        |                	
|                                                                  |                	
| Merkle Root:                                                     |	
| 0000000000000000000000000000000000000000000000000000000000000000 |                	
|                                                                  |                	
| Transações:                                                      |	
| 0                                                                |                	
|                                                                  |                	
| Hash do último bloco:                                            |	
| ea1d3930d2d494cfec7e030679f74cbe997f1fc0eeadeb67a24f1943d104b723 |                	
 ------------------------------------------------------------------	
                                A                                    	
                                |                                    	
 __________________________________________________________________	
| ea1d3930d2d494cfec7e030679f74cbe997f1fc0eeadeb67a24f1943d104b723 |                	
 ------------------------------------------------------------------                	
| Índice:         Timestamp:              Nonce:                   |	
| 2               1566323766              0                        |                	
|                                                                  |                	
| Merkle Root:                                                     |	
| 0000000000000000000000000000000000000000000000000000000000000000 |                	
|                                                                  |                	
| Transações:                                                      |	
| 0                                                                |                	
|                                                                  |                	
| Hash do último bloco:                                            |	
| e41cd82c0f0556dbee53a037be6871048005cda39140fde5b5deeaaf66e8a52b |                	
 ------------------------------------------------------------------	
                                A                                    	
                                |                                    	
 __________________________________________________________________	
| e41cd82c0f0556dbee53a037be6871048005cda39140fde5b5deeaaf66e8a52b |                	
 ------------------------------------------------------------------                	
| Índice:         Timestamp:              Nonce:                   |	
| 1               1566323766              0                        |                	
|                                                                  |                	
| Merkle Root:                                                     |	
| 0000000000000000000000000000000000000000000000000000000000000000 |                	
|                                                                  |                	
| Transações:                                                      |	
| 0                                                                |                	
|                                                                  |                	
| Hash do último bloco:                                            |	
| 0ce9ea8b4e967cc39b7db116164d0c067083ff351c21ee0454f9eda672be59a7 |                	
 ------------------------------------------------------------------	
                                A                                    	
                                |                                    	
 __________________________________________________________________	
| 0ce9ea8b4e967cc39b7db116164d0c067083ff351c21ee0454f9eda672be59a7 |                	
 ------------------------------------------------------------------                	
| Índice:         Timestamp:              Nonce:                   |	
| 0               1566323766              0                        |                	
|                                                                  |                	
| Merkle Root:                                                     |	
| 0000000000000000000000000000000000000000000000000000000000000000 |                	
|                                                                  |                	
| Transações:                                                      |	
| 0                                                                |                	
|                                                                  |                	
| Hash do último bloco:                                            |	
| 0000000000000000000000000000000000000000000000000000000000000000 |                	
 ------------------------------------------------------------------	
```

## Dicas

- Sempre utilize seus métodos previamente implementados para auxiliar a implementação dos novos. **Evite repetição de código**.
- [https://docs.python.org/3/library/time.html]

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
