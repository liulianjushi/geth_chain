from web3 import Web3, HTTPProvider
# enode://80d72840bc1a3d4207d932c7d862c521e188ec137efd2e7de48d2673e82c128e2737410381553183efadfa449cf3888a15cb03ce920dcb3d4d20a2de9cab3be9@127.0.0.1:30303?discport=0
# 连接钱包地址

# # 结果为true表示连接成功
# connect = web3.is_connected()
# # print(connect)
# print(web3.eth.accounts)
# print(web3.geth.admin.node_info()["enode"])

# print(web3.eth.get_block(300))

providers=["8.136.104.96","47.122.6.120","47.122.6.14"]
master_web3 = Web3(HTTPProvider(f"http://{providers[0]}:7545"))
master_enode=master_web3.geth.admin.node_info()["enode"].replace("127.0.0.1",f'{providers[0]}')

for provider in providers[1:]:
    node_web3 = Web3(HTTPProvider(f"http://{provider}:7545"))
    node_enode=node_web3.geth.admin.node_info()["enode"].replace("127.0.0.1",provider)
    master_web3.geth.admin.add_peer(node_enode)
    print(node_enode)
print(master_web3.geth.admin.peers())

# node_web3 = Web3(HTTPProvider(f"http://8.136.104.96:7545"))
# print(node_web3.eth.get_block(12103))
# print(node_web3.eth.get_transaction("0x7d5a6c7f8783b91239257ffe63fd84a6c3bb5c3aac30648f3212042861d6ec39"))
# print(node_web3.geth.miner.start())
# print(node_web3.eth.mining)