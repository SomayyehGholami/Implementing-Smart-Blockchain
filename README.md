<div class="alert alert-success">
    <h1 align="center">Implementing a "Smart Blockchain" with python</h1>
    <h3 align="center"><a href="https://medium.com/@somayyeh_43305">By: Somayyeh Gholami & Mehran Kazeminia</a></h3>
</div>

<img src="https://github.com/SomayyehGholami/Implementing-Smart-Blockchain/blob/master/readme_image/r101.jpg"> 

# Introduction

Ten years ago, Bitcoin’s proof-of-work mechanism was a great idea for a pilot project and the launch of the first decentralized network as well. But this approach for long-term must be corrected, and for years, the amount of power consumed ( more than 50TWh per year ) by a country with ten million populations, cannot be dedicated for bitcoin transactions only. It’s extreme selfishness and not fair

The research published in Nature Climate Change (October 2018) even suggested that Bitcoin mining alone could push global warming “above 2 °C within less than three decades“. The electricity consumption of the proof-of-work mechanism used in the bitcoin network is huge. Meanwhile, a major share of mining operations is done with electricity from coal-fired power plants in China, cause increasing Bitcoin’s environmental problems and blockchain technology

Smart Blockchain is the new generation of Blockchain networks that will allow one or more smart contracts to collect accurate and flawless data from the successful transactions of a decentralized network at the moment of transaction occurrence, and simultaneously storing and registering these data in new blocks. Smart Blockchain needs neither the financial institution nor intermediary, in addition, there will be no task to do for miners and block producers in this technology. In other words, within Smart Blockchain, always one or more smart contracts like a financial institution, free of charge and automatically record and store transactions ‘data in new blocks.

### How does Smart Blockchain work?
In Smart Blockchain, one or more Block Producer Smart Contract (BPSC) is present in the decentralized network, and no successful transaction is performed without BPSC involvement. For a successful transaction in the network, first, the sender must send the cryptocurrency to the wallet of BPSC and then BPSC sends cryptocurrency automatically to the receiver. This simple action has led the BPSC to have all network transactions’ data accurately and flawlessly and then as an accurate and trust financial institution, record transactions’ data into a new block and add this new block to the end of the blockchain and so there will be no tasks to assign to miners and block producers.

Also, Smart Blockchain provides the possibility to classify transactions based on subject. For example, it allows trading of several types of cryptocurrency in a network consists of independent blockchains. This will be done by increasing the number of BPSCs in the network. The limitation and also important point is that transactions can be assigned to separate BPSCs that their subjects are not related to each other. For example, if we want a smart contract to give an award for every 100 LIKEs, so the Likes’ transactions and cryptocurrencies’ transactions of such project should be stored and registered by the single BPSC and into single Blockchain.

### What are the benefits of Smart Blockchain?
At the moment of transactions occurrence, the correct and flawless data of transactions are stored and registered. In this case, there is no need to generate some alternatives from a block like what they do in Bitcoin network, Ethereum network, etc., and then the miners choose the correct and valid block by spending so much money, consuming huge power electricity and using a variety of proof mechanisms.

Staggering power consumption is the result of the use of the proof-of-work mechanism or the proof-of-stake mechanism, or..... Which Smart Blockchain does not require any of them at all. Unfortunately, the electricity consumption of one single bitcoin’s transaction is 200,000 times more than electricity consumption of a one single VISA’s transaction. The annual electricity consumption used to store and register the entire Bitcoin’s transactions is more than 50 terawatts (1 TWh = 3 600 000 000 000 000 J) that is equal to the annual power consumption of a country with ten million populations. The study was published in October 2018 on global climate change, which showed that in less than three decades, Bitcoin mining could increase global temperatures more than 2 degrees Celsius.

Fortunately, Smart Blockchain transactions and regular Visa Card transactions won’t differ on power consumption. The data stored by the BPSC is flawless because it is registered at the moment of the transaction occurrence automatically and without human interference. Smart Blockchain simply can end the nightmare of spending extra tens TWh electricity.

By using Smart Blockchain, we should no longer be concerned about the fees of miners and block producers. BPSCs will automatically and freely carry out all the tasks of the miners. Also, Smart Blockchain scalability is not comparable to available one and can compete with the speed of Visa’s transactions.

### What is the use of Smart Blockchain?
irst use: In networks like Ethereum, EOS, etc. which is possible to register and deploy the smart contracts, simply we can set up a dedicated blockchain for each new smart contract. In this way, as soon as the new smart contract is launched, a BPSC will be launched, and from the very beginning, all of the transactions of a smart contract will be stored and registered into the BPSC’s ledger. In this case, the dedicated blockchain will not need any data from Ethereum blockchain, EOS, etc., and it will work independently. Meanwhile, at coding, this BPSC can be coded and launched separately, or BPSC codes can be imported into the desired smart contract codes.

Second use: For each Ethereum networks, EOS, and etc. that allow registering and deploying the smart contracts, the whole existing Blockchains can be replaced with Smart Blockchain. To do this, after launching a dedicated BPSC into the network, the precise and final status of all existing wallet is to be made available to the BPSC, Also thereafter all the subsequent network transactions will be done via BPSC.

Third use: If we want to use Smart Blockchain for networks such as Bitcoin which is not possible to set up any smart contract, we should first launch a new decentralized network that allows registration and deployment of smart contracts like the Ethereum network. Then, in this new network, we design and activate a block producer smart contract BPSC. After assuring of the functionality of BPSC on the new network, we must ask all Bitcoin owners to get the equivalent of their bitcoin, from the new Blockchain’s cryptocurrency, and at the same time, their initial bitcoin should be burned. These are done by the BPSC of a network, and the BPSC can record the initial balance of any wallet in the network and begin its work immediately.

Fourth use: Smart Blockchain can be used to launch entirely new blockchain and certainly everything can be designed from scratch. Meanwhile, regarding the Smart Blockchain’s features, we might soon see one or more non-decentralized global networks that include all types of cryptocurrencies and smart contracts with independent blockchain.

### More Information
https://www.soliset.com
https://www.newchains.info

<img src="https://github.com/SomayyehGholami/Implementing-Smart-Blockchain/blob/master/readme_image/r103.jpg">

# Implementing a "Smart Blockchain" with python
In this article, we are going to implement a simple and plain "smart blockchain" with Python language and compare it with a blockchain. We hope that by doing this, the main concepts and advantages of this technology will be more clearly specified and welcomed by the developers and the blockchain community. A Block Producer Smart Contract (BPSC) exists in a plain "smart blockchain" network. To make a successful transaction in the network, the sender must first transfer the cryptocurrency to the (BPSC) wallet, and immediately the (BPSC) will automatically send the same cryptocurrency to the final recipient's wallet. This seemingly simple task saves accurate and impervious data from all successful transactions in the (BPSC) Smart Contract. The present article was written in April 2020 by Somayeh Gholami and Mehran Kazeminia in two versions in English and Persian.

### Summary and conclusion:
To simulate the (BPSC) block producer smart contract, we considered a node with a port number 5000 and implemented the following three files:

bpsc101.py This version is not final and cannot be interacted with other nodes.

bpsc102.py This is the final version and all cases have been tested for this version. We tested the transaction request, the mining request, the request to send the last chain for the other nodes, and so on.

bpsc103.py This version is also final, but in this version, we have added a new feature to the previous version. That is, (BPSC) required to create a new block after each transaction and add that block to its chain.

The ports 5001 and 5002 have the representation of other network nodes. To simulate these nodes, we implemented the following two versions:

nodes_v1_5001.py and nodes_v1_5002.py
This version is according to "Smart Blockchain" technology and final. Although these nodes cannot produce blocks, they can do their transactions through (BPSC) and also receive the last chain from (BPSC).

nodes_v2_5001.py and nodes_v2_5002.py
This is also final, but in this version, we have added a new feature to the previous version. It means a simple blockchain (To store personal data) has been added to the previous code.


