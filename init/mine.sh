#!/bin/sh
cp -r /workspace/keystore/* ~/data/keystore/
geth --datadir ~/data/ --networkid 88 --http --http.addr 0.0.0.0 --http.port 7545 --port 30303 --http.api "admin,eth,miner,web3,personal,net,txpool,debug" --http.corsdomain "*" --mine --etherbase --unlock 0x23E53c3882B64B0907C831cFe7198c0a9a125e33 --password /workspace/password.txt  --allow-insecure-unlock  --nodiscover console

