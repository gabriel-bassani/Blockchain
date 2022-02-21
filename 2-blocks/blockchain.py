import hashlib
import json
from time import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.hash = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        # Implemente aqui o método para gerar o bloco Genesis, invocado no construtor da classe,
        # chamando o método createBlock() previamente implementado.
        # O índice do bloco gênesis deve ser 0 (zero), e o previousBlock dele ser 0x0, com 64 dígitos 
        # hexadecimais (256 bits), codificados como uma string.
        # O método deve retornar o bloco genesis criado.
        genesis_block = {
            'index': 0,
            'timestamp': time(),
            'nonce': 0,
            'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000',
            'previousHash': '0000000000000000000000000000000000000000000000000000000000000000',
            'transactions': []
        }


        self.chain.append(genesis_block)

        return genesis_block 

    def createBlock(self):
        # Implemente aqui o método para retornar um bloco (formato de dicionário).
        # Lembre que o hash do bloco anterior é o hash na verdade somente do CABEÇALHO do bloco anterior.
        # Inclua o bloco criado na lista `chain`, por enquanto não precisamos valida-lo.
        # O método deve retornar o bloco recém-criado.

        """
        if len(self.chain) == 0: 
            block = Blockchain.createGenesisBlock(self)
            #print(len(self.chain))
            self.chain.append(block)
        """

        if len(self.chain) > 0:
            #print('len(self.chain):', len(self.chain))
            #print('len(self.previousHash):', len(self.previousHash))

            #print('previousHash test0:', self.previousHash[len(self.previousHash) - 1])


            
            


            #hashTmp = str(len(self.chain)) + str(self.timestamp[len(self.chain)]) + self.nonce[len(self.chain)] + self.merkleRoot[len(self.chain)]
            hashTmp = self.chain[len(self.chain) - 1].copy()
            hashTmp.pop('transactions')
            hash = Blockchain.generateHash(hashTmp)
            #print('hash', hash)


            block = {
                'index': len(self.chain),
                'timestamp': time(),
                'nonce': '0',
                'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000',
                'previousHash': hash,
                'transactions': []
            }
            
            self.chain.append(block)
        

        return block

    @staticmethod
    def getBlockID(block):
        # Implemente aqui um método auxiliar para gerar o ID de um bloco passado como parâmetro.
        # Lembra o que é o ID de um bloco?!?! Hash do seu cabeçalho! 
        # Dica: as transações de um bloco não fazem parte de seu cabeçalho...
        # Dica2: não deixe de usar seus método previamente implementados.


        #hashTmp = str(block['index']) + str(block['timestamp']) + str(block['nonce']) + block['merkleRoot'] + block['previousHash']
        #hashTmp = str(block['index']) + block['merkleRoot']  + block['previousHash']+ str(block['nonce'])+ str(block['timestamp'])
        #hashTmp = str(block['timestamp']) + str(block['index']) + str(block['nonce']) + block['merkleRoot'] + block['previousHash']
        hashTmp = block.copy()
        hashTmp.pop('transactions')

        #print('hashTmp:', hashTmp)
        block_id = Blockchain.generateHash(hashTmp)
        #print('block_id:', block_id)


        return block_id

    @staticmethod
    def generateHash(data):
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    def printChain(self):
        # Implemente aqui um método para imprimir de maneira verbosa e intuitiva o blockchain atual.
        for x in self.chain:
            tmp = Blockchain.getBlockID(x)

            print(' __________________________________________________________________ ')
            print('|', tmp, '|')
            print(' ------------------------------------------------------------------ ')
            print('|', x['index'], '\t\t', x['timestamp'], '\t\t', x['nonce'], '\t\t', '  |')
            print('|                                                                  |')
            print('| Merkle Root:                                                     |')
            print('|', x['merkleRoot'], '|')
            print('|                                                                  |')
            print('| Transações:                                                      |')
            print('| 0                                                                |')
            print('|                                                                  |')
            print('| Hash do último bloco:                                            |')
            print('|', x['previousHash'], '|')
            print('|', tmp, '|')
            print(' ------------------------------------------------------------------ ')
            print('                                A                                    	')
            print('                                |                                    	')

        pass

# Teste, fique a vontade para modificar.
blockchain = Blockchain()
for x in range(0, 3): blockchain.createBlock()

blockchain.printChain()
