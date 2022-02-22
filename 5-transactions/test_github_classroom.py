# ATENÇÃO! NÃO EDITEM ESTE ARQUIVO!
# Teste automatizado (GitHub Classroom).

from blockchain import Blockchain, json


def test_blockchain_hashing():
    assert(Blockchain.generateHash({'nome': "Walter White", 'idade': 45})
           == "ef9ef3225f42aed9de1581f19c729083fce7f764b94c3fdbfb261c27399d5fff")
    assert(Blockchain.generateHash("blockchain@imd") ==
           "4031946b26fc93498b341b9b856b041d4c883d063e8207b9e478f01667259204")
    assert(Blockchain.generateHash({'universidade': "UFRN", 'departamento': "IMD", 'curso': "IMD0293"})
           == "a375dedc09a38a78affa1d5e92a181e2d19d28cb5bd64e9c40d5ff15a5ee5c8d")


def test_blockchain_block_fields():
    blockchain = Blockchain()
    block = blockchain.createBlock()
    assert(('index' in block) and ('timestamp' in block) and ('transactions' in block) and (
        'merkleRoot' in block) and ('nonce' in block) and ('previousHash' in block))


def test_blockchain_block_field_lengths():
    blockchain = Blockchain()
    block = blockchain.createBlock()
    assert(len(block['merkleRoot']) == 64)
    assert(len(block['previousHash']) == 64)


def test_blockchain_genesis_block():
    blockchain = Blockchain()
    assert(len(blockchain.chain) == 1)
    genesis = blockchain.chain[-1]
    assert(genesis['index'] == 0 or genesis['index'] == 1)
    assert(genesis['previousHash'] == '0'*64)


def test_block_id_calculation():
    block = {
        "index": 3,
        "merkleRoot": "0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": 0,
        "previousHash": "881861693f417984563977b5f42145d55c0d2dde214a04c16ac0db9b38d1e7e0",
        "timestamp": 1635946370,
        "transactions": []
    }
    assert(Blockchain.getBlockID(block) ==
           "034ef3b2ecfe97ff1ed459584992e615592721ed2e0d347c91ebf866b5f98037")


def test_blockchain_block_previous_hash():
    blockchain = Blockchain()
    block_0 = blockchain.chain[-1]
    block_1 = blockchain.createBlock()
    block_2 = blockchain.createBlock()
    block_3 = blockchain.createBlock()
    assert(block_1['previousHash'] == Blockchain.getBlockID(block_0))
    assert(block_2['previousHash'] == Blockchain.getBlockID(block_1))
    assert(block_3['previousHash'] == Blockchain.getBlockID(block_2))


def test_is_valid_proof():
    result_1_true = Blockchain.isValidProof({'index': 1, 'timestamp': 1637007513, 'transactions': [], 'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000', 'nonce': 0, 'previousHash': '000067f74e13a541df3233b89d46c917834a41e5ac75bb4b2aeed019a075f2ab'}, 102208)
    result_1_false = Blockchain.isValidProof({'index': 1, 'timestamp': 1637007513, 'transactions': [], 'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000', 'nonce': 0, 'previousHash': '000067f74e13a541df3233b89d46c917834a41e5ac75bb4b2aeed019a075f2ab'}, 102207)
    result_2_true = Blockchain.isValidProof({'index': 4, 'timestamp': 1637007516, 'transactions': [], 'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000', 'nonce': 50650, 'previousHash': '0000f70ea3170594c1a853e7b9e1d7978301177185c6bbf5994747152ac1bc6a'}, 50650)
    result_2_false = Blockchain.isValidProof({'index': 4, 'timestamp': 1637007516, 'transactions': [], 'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000', 'nonce': 50650, 'previousHash': '0000f70ea3170594c1a853e7b9e1d7978301177185c6bbf5994747152ac1bc6a'}, 50651)
    assert(result_1_true == True and result_1_false == False)
    assert(result_2_true == True and result_2_false == False)


def test_mine():
    block = {'index': 7, 'timestamp': 1637008057, 'transactions': [], 'merkleRoot': '0000000000000000000000000000000000000000000000000000000000000000', 'nonce': 0, 'previousHash': '00009aae5ad52e746ae7e7c5b58bbc4062eda59d3088b0a573899831280e2753'}
    blockchain = Blockchain()
    nonce = blockchain.mineProofOfWork(block)
    assert(nonce == 210)


def test_sign():
    privKey = 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U'
    message = 'Bora assinar essa mensagem?'
    signature = Blockchain.sign(privKey, message)
    assert(signature == "ILh7tecvUPuvjm+NOmZPd/eeFujagpG/Ztc34dXmeTccWDzMGb1AVu5HjgIBAHj0aJB31phf7EjpS5NnqRKo5Ks=")


def test_verify():
    addr = '19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF'
    message = 'Bora assinar essa mensagem?'
    signature = "ILh7tecvUPuvjm+NOmZPd/eeFujagpG/Ztc34dXmeTccWDzMGb1AVu5HjgIBAHj0aJB31phf7EjpS5NnqRKo5Ks="
    assert(Blockchain.verifySignature(addr, signature, message) == True)


def test_blockchain_tx_fields():
    blockchain = Blockchain()
    tx = blockchain.createTransaction('19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF', '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N', 0.1, 1637953954, 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U') 
    assert(('sender' in tx) and ('recipient' in tx) and ('amount' in tx) and ('timestamp' in tx) and ('signature' in tx))


def test_blockchain_tx_signature():
    blockchain = Blockchain()
    tx = blockchain.createTransaction('19sXoSbfcQD9K66f5hwP5vLwsaRyKLPgXF', '1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N', 0.1, 1637953954, 'L1US57sChKZeyXrev9q7tFm2dgA2ktJe2NP3xzXRv6wizom5MN1U') 
    addr = tx['sender']
    signature = tx['signature']
    tx.pop("signature", None)
    message = json.dumps(tx, sort_keys=True)
    assert(Blockchain.verifySignature(addr, signature, message) == True)


def test_blockchain_merkleroot():
    mr = Blockchain.generateMerkleRoot(['a', 'b', 'c', 'd'])
    assert(mr == "dc0b6133e27657993a9285058d7d50ecb7919a54743ce16e75deeb8b451c6e0e")
    mr = Blockchain.generateMerkleRoot(['a', 'b', 'c'])
    assert(mr == "ab2a9aa202d5de098173c852a81d49a625bee64279d3c34788f098518beaf360")
