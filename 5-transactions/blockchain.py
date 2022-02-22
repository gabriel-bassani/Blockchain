import hashlib
import json
from time import time
import copy
import random
import bitcoinlib # pip install bitcoin

DIFFICULTY = 4 # Quantidade de zeros (em hex) iniciais no hash valido.

class Blockchain(object):
    '''Classe utilizada para representar um blockchain privado baseado no protocolo Bitcoin.'''

    def __init__(self):
        self.chain = []
        self.memPool = []
        self.createGenesisBlock()

    def createGenesisBlock(self):
        '''Cria, minera e retorna o bloco gênesis do blockchain. Chamado somente no construtor.'''
        genesis_block = self.createBlock()
        self.mineProofOfWork(self.prevBlock)
        return genesis_block

    def createBlock(self):
        '''Cria um novo bloco, inclui todas as transações pendentes e adiciona ao chain. O bloco ainda não tem nonce válido.'''

        print('mempool:', self.memPool)
        block = {
            'index': len(self.chain),
            'timestamp': int(time()),
            'transactions': self.memPool,
            'merkleRoot': self.generateMerkleRoot(self.memPool) if (len(self.memPool)) else '0'*64,
            'nonce': 0,
            'previousHash': self.getBlockID(self.chain[-1]) if (len(self.chain)) else '0'*64
        }

        #
        #print('block:', block)
        #

        self.memPool = []
        self.chain.append(block)
        return block

    def mineProofOfWork(self, block):
        '''Retorna um nonce válido para o bloco passado como argumento.'''
        nonce = 0
        while self.isValidProof(block, nonce) is False:
            nonce += 1
        return nonce

    @staticmethod
    def isValidProof(block, nonce):
        '''Retorna `True` caso o nonce passado como argumento seja válido para o block passado como argumento, `False` caso contrário.'''
        block['nonce'] = nonce
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        guessedHash = Blockchain.generateHash(blockCopy)
        return guessedHash[:DIFFICULTY] == '0' * DIFFICULTY 

    def createTransaction(self, sender, recipient, amount, timestamp, privWifKey):
        '''Cria, insere no mempool e retorna uma nova transação, assinada pela chave privada WIF do remetente.'''
        # IMPLEMENTE AQUI!


        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": timestamp,
        }
        mensagem = json.dumps(transaction, sort_keys=True).encode()

        assinatura = Blockchain.sign(privWifKey, mensagem)
        print('assinatura:', assinatura)
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": timestamp,
            "signature": assinatura
        }
        self.memPool.append(transaction)

        return transaction

    @staticmethod
    def generateMerkleRoot(transactions):
        '''Retorna a Merkle Root de um conjunto de transações.'''
        # IMPLEMENTE AQUI!
        #print('transactions[0]:', transactions[0], 'transactions[1]:', transactions[1])
        if transactions:
            leafHash = []
            for trans in transactions:
                leafHash.append(Blockchain.generateHash(trans))
            if(len(leafHash) % 2 != 0):
                leafHash.append(leafHash[len(leafHash) - 1])

            i = 0
            hash1 = leafHash
            hash2 = []

            while(len(hash1) > 1):
                for x in hash1:
                    if i % 2 == 0:
                        if(i == len(hash1) - 1): break
                        hash2.append(Blockchain.generateHash(hash1[i]+hash1[i+1]))
                        i = i + 1
                        continue
                    i = i + 1
                hash1 = hash2
                hash2 = []
                i = 0


            return hash1[0]

    @staticmethod
    def generateHash(data):
        '''Retorna a hash SHA256 dos dados passados como argumento.'''
        blkSerial = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(blkSerial).hexdigest()

    @staticmethod
    def getBlockID(block):
        '''Retorna o ID do bloco passado como argumento. O ID de um bloco é o hash do seu cabeçalho.'''
        blockCopy = copy.copy(block)
        blockCopy.pop("transactions", None)
        return Blockchain.generateHash(blockCopy)

    @property
    def prevBlock(self):
        '''Retorna o último bloco da chain.'''
        return self.chain[-1]

    @staticmethod
    def getWifCompressedPrivateKey(private_key=None):
        '''Retorna a chave privada no formato WIF-compressed da chave privada hex.'''
        if private_key is None:
            private_key = bitcoinlib.random_key()
        return bitcoinlib.encode_privkey(bitcoinlib.decode_privkey((private_key + '01'), 'hex'), 'wif')
        
    @staticmethod
    def getBitcoinAddressFromWifCompressed(wif_pkey):
        '''Retorna o endereço Bitcoin da chave privada WIF-compressed.'''
        return bitcoinlib.pubtoaddr(bitcoinlib.privkey_to_pubkey(wif_pkey))

    @staticmethod
    def sign(wifCompressedPrivKey, message):
        '''Retorna a assinatura digital da mensagem e a respectiva chave privada WIF-compressed.'''
        return bitcoinlib.ecdsa_sign(message, wifCompressedPrivKey)

    @staticmethod
    def verifySignature(address, signature, message):
        '''Verifica se a assinatura é correspondente a mensagem e o endereço BTC.
        Você pode verificar aqui também: https://tools.bitcoin.com/verify-message/'''

        print('address:', address, '\nsignature:', signature, '\nmessage:', message)


        return bitcoinlib.ecdsa_verify(message, signature, address)
    
    def printChain(self):
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

        pass # Mantenha seu método de impressão do blockchain feito nas práticas passadas.


# Teste

blockchain = Blockchain()

sender = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF' # Você pode gerar novos endereços BTC em https://www.bitaddress.org/
recipient = '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N' # Você pode gerar novos endereços BTC em https://www.bitaddress.org/

for x in range(0, 4): 
    for y in range(0, random.randint(1,4)) : 
        timestamp = int(time())
        amount = random.uniform(0.00000001, 100)
        blockchain.createTransaction(sender, # remetente da transação;
                                    recipient, # destinatário da transação;
                                    amount, # valor a ser transferido do endereço do sender para o endereço do recipient;
                                    timestamp, # data (formato unix) de criação da transação;
                                    'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U') # chave privada WIF de quem envia
    blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)

blockchain.printChain()
