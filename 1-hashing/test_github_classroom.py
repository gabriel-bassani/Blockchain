## ATENÇÃO! NÃO EDITEM ESTE ARQUIVO!
# Teste automatizado (GitHub Classroom).

from blockchain import *

def test_blockchain_hashing():
    assert(Blockchain.generateHash({'nome': "Walter White", 'idade': 45})=="ef9ef3225f42aed9de1581f19c729083fce7f764b94c3fdbfb261c27399d5fff")
    assert(Blockchain.generateHash("blockchain@imd")=="4031946b26fc93498b341b9b856b041d4c883d063e8207b9e478f01667259204")
    assert(Blockchain.generateHash({'universidade': "UFRN", 'departamento': "IMD", 'curso': "IMD0293"})=="a375dedc09a38a78affa1d5e92a181e2d19d28cb5bd64e9c40d5ff15a5ee5c8d")
