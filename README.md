# BlockChain_Record
A simple blockchain to record the operation records on the distributed mongodb
# 初始化区块链

```Bash
cd blockchain
./init.sh                          #清空原有文件夹，初始化创世块文件、
./start.sh                         #开始运行区块链（也可以以将其用nohup挂载在后台运行就不用在下面步骤新开一个端口）
```
区块链运行后在 chain-data 目录下会有 geth.ipc 文件，新开一个端口执行以下命令

```Bash
cd chain-data
geth attach geth.ipc
```

# 为合约的部署准备条件
miner.start()
miner.stop()


# Pass the parameter to the test.py
