"""
Smart Blockchain - Nodes
Created on Mon Mar 16 23:31:42 2020
@author: Somayyeh & Mehran

Filename:  nodes_v1_5001.py 
Mine: By BPSC
Port: 5001

In “Smart Blockchain”, one or more block producers smart contract (BPSC) is present in the network, 
and no successful transaction is performed without BPSC involvement. For a successful transaction 
in the network, first, the sender must send the cryptocurrency to the wallet of BPSC and then BPSC 
sends cryptocurrency automatically to the receiver. This simple action has led the BPSC to have all 
network transactions’ data accurately and flawlessly and then as an accurate and trust financial 
institution, record transactions’ data into a new block and add this new block to the end of the 
blockchain so there would be no task for miners in “Smart Blockchain”.

"""

from urllib.parse import urlparse

import requests
from flask import Flask, jsonify, request


class Smart_Blockchain:
    def __init__(self):
        self.chain = []
        self.nodes = set()


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

    
# Instantiate the Node
app = Flask(__name__)

# Instantiate the Smart_Blockchain
blockchain = Smart_Blockchain()


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

