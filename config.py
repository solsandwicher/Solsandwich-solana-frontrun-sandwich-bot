import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS')
    PRIVATE_KEY = os.getenv('PRIVATE_KEY')
    SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL')
    QUICKNODE_RPC_URL = os.getenv('QUICKNODE_RPC_URL')
    SOLANA_WS_URL = os.getenv('SOLANA_WS_URL')  # WebSocket URL for Solana
    QUICKNODE_WS_URL = os.getenv('QUICKNODE_WS_URL')  # WebSocket URL for QuickNode
