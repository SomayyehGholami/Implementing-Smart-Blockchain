import hashlib
import json
from time import time

class Smart_Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash):
        """
        Create a new Block in the Smart Blockchain
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block


    def new_transaction(self, sender, amount, recipient):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: Address of the Sender
        :param amount_send: The amount sent by the sender
        :param bpsc: Address of the Smart contract (bpsc)
        :param amount_bpsc: The amount received by bpsc (Transaction fees)
        :param recipient: Address of the Recipient
        :param amount_receive: The amount received by the recipient
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'amount_send': amount,
             
            'bpsc': 'bpsc_wallet_address', # Block Producer Smart Contract (bpsc)
            'amount_bpsc': amount * 0.00005, # Transaction fees
            
            'recipient': recipient,
            'amount_receive': amount * 0.99995,
        })

        return self.last_block['index'] + 1
        

    @property
    def last_block(self):
        return self.chain[-1]


    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    