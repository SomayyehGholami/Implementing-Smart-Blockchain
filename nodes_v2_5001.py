"""
Smart Blockchain - Nodes
Created on Tue Mar 17 09:05:17 2020
@author: Somayyeh & Mehran

Filename:  nodes_v2_5001.py 
Mine: By BPSC & Selfie chain
Port: 5001

In “Smart Blockchain”, one or more block producers smart contract (BPSC) is present in the network, 
and no successful transaction is performed without BPSC involvement. For a successful transaction 
in the network, first, the sender must send the cryptocurrency to the wallet of BPSC and then BPSC 
sends cryptocurrency automatically to the receiver. This simple action has led the BPSC to have all 
network transactions’ data accurately and flawlessly and then as an accurate and trust financial 
institution, record transactions’ data into a new block and add this new block to the end of the 
blockchain so there would be no task for miners in “Smart Blockchain”.

"""

import hashlib
import json
from time import time
from urllib.parse import urlparse

import requests
from flask import Flask, jsonify, request


class Smart_Blockchain:
    def __init__(self):
        self.current_information = []        
        self.chain = []
        self.chain2 = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash='1')
        
        
    def register_node(self, address):
        """
        Add a new node to the list of nodes
        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def smart_chain(self):
        """
        All nodes can receive the smart_chain
        """
        
        schain = None       
        response = requests.get(f'http://127.0.0.1:5000/chain')
        
        if response.status_code == 200:
            chain = response.json()['chain']                
            schain = chain

        # Replace our chain
        if schain:
            self.chain = schain
            return True

        return False


    def new_block(self, previous_hash):
        """
        Create a new Block in the Smart Blockchain
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index2': len(self.chain2) + 1,
            'timestamp': time(),
            'information': self.current_information,
            'previous_hash': previous_hash or self.hash(self.chain2[-1]),
        }

        # Reset the current list of transactions
        self.current_information = []

        self.chain2.append(block)
        return block

        
    def new_information(self, information):
        """
        Creates a new information
        :param information: Your information
        :return: The index of the Block that will hold this information
        """
        self.current_information.append({'information': information })


        return self.last_block['index2'] + 1


    @property
    def last_block(self):
        return self.chain2[-1]


    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

            
# Instantiate the Node
app = Flask(__name__)

# Instantiate the Smart_Blockchain
blockchain = Smart_Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(previous_hash)

    response = {
        'message': "New Block Forged",
        'index2': block['index2'],
        'information': block['information'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/information/new', methods=['POST'])
def new_information():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['information']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new information
    index = blockchain.new_information(values['information'])
    
    response = {'message': f'information will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain2', methods=['GET'])
def full_chain2():
    response = {
        'chain2': blockchain.chain2,
        'length': len(blockchain.chain2),
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/smart/chain', methods=['GET'])
def smart_chain():
    replaced = blockchain.smart_chain()

    if replaced:    
        response = {
            'message': 'Smart chain update by bpsc',
            'smart chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
    else:
        response = {
            'message': 'Unsuccessful: Please try again',
            'old chain': blockchain.chain,
            'length': len(blockchain.chain)            
        }
        
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)




