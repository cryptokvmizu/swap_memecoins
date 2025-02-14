from web3 import Web3
import json
import os

# Replace with your Ethereum node provider (Infura, Alchemy, etc.)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection is successful
if not web3.is_connected():
    raise Exception("Failed to connect to Ethereum network")

# Wallet details
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
WALLET_ADDRESS = web3.to_checksum_address("YOUR_WALLET_ADDRESS")

# Uniswap V2 Router address
UNISWAP_ROUTER_ADDRESS = web3.to_checksum_address("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

# Load Uniswap V2 Router ABI
with open("uniswap_v2_router_abi.json", "r") as f:
    UNISWAP_ROUTER_ABI = json.load(f)

router_contract = web3.eth.contract(address=UNISWAP_ROUTER_ADDRESS, abi=UNISWAP_ROUTER_ABI)

# Tokens (replace with actual token contract addresses)
TOKEN_IN = web3.to_checksum_address("0xTOKEN_IN_ADDRESS")  # Example: WETH
TOKEN_OUT = web3.to_checksum_address("0xTOKEN_OUT_ADDRESS")  # Example: MEMECOIN
AMOUNT_IN_WEI = web3.to_wei(0.01, "ether")  # Adjust amount as needed

def swap_tokens():
    # Approve token transfer
    token_contract = web3.eth.contract(address=TOKEN_IN, abi=json.load(open("erc20_abi.json")))
    approve_txn = token_contract.functions.approve(
        UNISWAP_ROUTER_ADDRESS, AMOUNT_IN_WEI
    ).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": 100000,
        "gasPrice": web3.to_wei("50", "gwei"),
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS),
    })
    signed_approve_txn = web3.eth.account.sign_transaction(approve_txn, PRIVATE_KEY)
    web3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
    print("Token approved")
    
    # Swap tokens
    deadline = web3.eth.get_block('latest')['timestamp'] + 60  # 1-minute deadline
    swap_txn = router_contract.functions.swapExactTokensForTokens(
        AMOUNT_IN_WEI,  # Amount of input token
        0,  # Minimum output amount (set to 0 for simplicity; use slippage control in prod)
        [TOKEN_IN, TOKEN_OUT],
        WALLET_ADDRESS,
        deadline
    ).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": 200000,
        "gasPrice": web3.to_wei("50", "gwei"),
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS),
    })
    signed_swap_txn = web3.eth.account.sign_transaction(swap_txn, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
    print(f"Swap transaction sent: {web3.to_hex(tx_hash)}")

if __name__ == "__main__":
    swap_tokens()
