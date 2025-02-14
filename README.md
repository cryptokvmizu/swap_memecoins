# Swap Memecoins on Ethereum Mainnet

This Python script enables swapping memecoins on the Ethereum mainnet using the Uniswap V2 protocol via Web3.py.

## Features
- Connects to Ethereum mainnet via Infura.
- Approves token transfers.
- Executes token swaps using Uniswap V2.
- Configurable input tokens, output tokens, and gas fees.

## Requirements
- Python 3.7+
- Web3.py
- Infura or other Ethereum node provider

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourrepo/swap-memecoins.git
   cd swap-memecoins
   ```
2. Install dependencies:
   ```sh
   pip install web3
   ```
3. Obtain an Infura API key and update the `INFURA_URL` in the script.
4. Set up your Ethereum wallet details (private key and address).

## Usage
1. Ensure you have ETH for gas fees.
2. Modify `TOKEN_IN` and `TOKEN_OUT` with the correct contract addresses.
3. Run the script:
   ```sh
   python swap_memecoins.py
   ```

## Security Considerations
- Never hardcode private keys in the script. Use environment variables or a secure key vault.
- Be cautious of slippage when swapping tokens.

## License
This project is licensed under the MIT License.
