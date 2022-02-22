[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6412753&assignment_repo_type=AssignmentRepo)
# Atividade: Proof-of-Work (`03-pow`)

Esta atividade tem como objetivo implementar o algoritmo responsável por minerar um novo bloco ao encontrar um *nonce* válido para os dados de entrada (*proof-of-work*), considerando uma dificuldade fixa.

## Metodologia e Avaliação

O desenvolvimento das atividades avaliativas deve ser realizada individualmente, em computador pessoal ou em computador do laboratório, com livre consulta a recursos na internet (*consulta != cópia*) e discussão entre colegas. Utilize a IDE de sua preferência (sugestão: Visual Studio Code).

As atividades são cumulativas, de forma que ao final teremos um blockchain funcional usando as técnicas e os conceitos téoricos vistos em sala de aula.

## Instruções de submissão

Submissão deve ser feita a partir do GitHub Classroom até às 23:59 do dia 21/11/2021. Basta realizar o *commit* do seu arquivo `blockchain.py` no repositório privado criado para você a partir do link disponibilizado (associe sua conta GitHub ao seu nome na plataforma). Qualquer dúvida nesta etapa consulte o professor no Discord. **Atenção!** Não mexer/editar o arquivo `test_github_classroom.py`.

## Instalação

Baixe o arquivo `./blockchain.py` para obter o *boilerplate* para esta atividade. Caso seja necessário, utilize o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os módulos necessários. Todos os *boilerplates* são compatíveis com o Python 3+.

## Descrição

A atividade consiste na implementação do método `mineProofOfWork(block)` para retornar e atribuir um *nonce* válido para o último bloco criado. A dificuldade é fixa e definida pela variável `DIFFICULTY`, que representa a quantidade de zeros em hexadecimais exigidas no início do *hash* do cabeçalho do bloco. De maneira sucinta, todo bloco criado deverá passar pelo processo de mineração para que seja válido. A assinatura do método é definida como:

```python
def mineProofOfWork(self, block):
```

Para auxiliar o processo de mineração no desenvolvimento do método anterior, implemente também o método `isValidProof(block, nonce)`, que retorna `True` caso o `nonce` passado como argumento é válido para o bloco `block` passado também como argumento.

```python
def isValidProof(block, nonce):
```

A dificuldade definida para essa atividade é que o *hash* do cabeçalho do bloco deve ser menor que o alvo (*target*) abaixo:

```alvo = 0x0001000000000000000000000000000000000000000000000000000000000000```

Isso quer dizer que o *hash* encontrado deve ter um prefixo de quatro caracteres hexadecimais 0's. Exemplos:

- **[INVÁLIDO]** 00078112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
- **[INVÁLIDO]** 0001e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d
- **[VÁLIDO]**   00002c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6

## Dicas

Note que, para facilitar, foi criado uma propriedade (*@property*) chamada `prevBlock` que retorna o último bloco incluído na lista `chain`.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
