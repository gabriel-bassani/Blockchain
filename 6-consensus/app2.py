from flask import Flask, request
from blockchain import Blockchain
import requests
from time import time
import json

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/transactions/create', methods=['POST'])
def transactionsCreate():
    transactions = request.get_json(force=True)
    sender = transactions['sender']
    recipient =  transactions['recipient']
    amount = transactions['amount']
    timestamp = int(time())
    privWifKey = transactions['privWifKey']
    blockchain.createTransaction(sender, recipient , amount, timestamp, privWifKey)
    lastMemPool = json.dumps(blockchain.memPool[-1], sort_keys=True)
    return lastMemPool

@app.route('/transactions/mempool', methods=['GET'])
def transitionsMempool():
    mempool = json.dumps(blockchain.memPool, sort_keys=True)
    return mempool

@app.route('/mine', methods=['GET'])
def mine():
    cheateBlock = blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)
    return json.dumps(cheateBlock, sort_keys=True)

@app.route('/chain', methods=['GET'])
def chain():
    chain = json.dumps(blockchain.chain, sort_keys=True)
    return chain

@app.route('/nodes/register', methods=['POST'])
def registerNode():
    nodes = request.get_json(force=True)	
    node = nodes["node"]
    blockchain.nodes.add(node) 	
    return json.dumps([node for node in blockchain.nodes], sort_keys=True)


@app.route('/nodes/resolve', methods=['GET'])
def resolveNode():
    resolveConflicts = blockchain.resolveConflicts()
    return json.dumps(resolveConflicts, sort_keys=True)

if __name__ == '__main__':
    app.run(port=5001)