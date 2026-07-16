import time
import os
from datetime import datetime
from web3 import Web3
from eth_account import Account

BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'
BOLD = '\033[1m'

# GIWA Sepolia Testnet
INFURA_URL = "https://sepolia-rpc.giwa.io"
PRIVATE_KEY = "YOURPRIVATE_KEY"

# Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
account = Account.from_key(PRIVATE_KEY)

# Connection
if not w3.is_connected():
    print("404 GIWA Testnet")
    exit()

os.system('clear')

print(f"Connected GIWA Testnet, Chain ID: {w3.eth.chain_id}")
print(f"Address: {account.address}")
print(f"Balance: {w3.from_wei(w3.eth.get_balance(account.address), 'ether')} ETH\n")

def create_contract():
    """contract GIWA Sepolia Testnet"""
    try:
        contract_bytecode = "0x60806040527308b9591878aae2ebb2aca5f3ec6dcc1c225b7e4e5f5f6101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505f341115610129575f5f5f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16346040516100a4906101cb565b5f6040518083038185875af1925050503d805f81146100de576040519150601f19603f3d011682016040523d82523d5f602084013e6100e3565b606091505b5050905080610127576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161011e90610239565b60405180910390fd5b505b3373ffffffffffffffffffffffffffffffffffffffff167f0f7cceb5b8900763db0b46908960abf22a5d055a4a7395b6b83862d93f241d21345f5f9054906101000a900473ffffffffffffffffffffffffffffffffffffffff166040516101919291906102ae565b60405180910390a26102d5565b5f81905092915050565b50565b5f6101b65f8361019e565b91506101c1826101a8565b5f82019050919050565b5f6101d5826101ab565b9150819050919050565b5f82825260208201905092915050565b7f6661696c656400000000000000000000000000000000000000000000000000005f82015250565b5f6102236006836101df565b915061022e826101ef565b602082019050919050565b5f6020820190508181035f83015261025081610217565b9050919050565b5f819050919050565b61026981610257565b82525050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6102988261026f565b9050919050565b6102a88161028e565b82525050565b5f6040820190506102c15f830185610260565b6102ce602083018461029f565b9392505050565b603e806102e15f395ff3fe60806040525f5ffdfea2646970667358221220836167b40148edc65dce7aa4c3416f2c4b640b50483fa57dec2183b10ba7e1ef64736f6c634300081e0033"
        
        nonce = w3.eth.get_transaction_count(account.address, 'pending')
        print(f"Transaction Count: {nonce}")
        
        gas_price = w3.eth.gas_price
        print(f"Gas Price: {w3.from_wei(gas_price, 'gwei')} Gwei")
        
        try:
            estimated_gas = w3.eth.estimate_gas({
                'from': account.address,
                'data': contract_bytecode,
                'nonce': nonce,
            })
            print(f"Estimated Gas: {estimated_gas}")
        except Exception as e:
            print(f"Gas estimation error: {e}")
            estimated_gas = 1000000
        
        transaction = {
            'nonce': nonce,
            'gas': 3000000,
            'gasPrice': gas_price,
            'data': contract_bytecode,
        }
        
        signed_txn = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"Tx Hash: {tx_hash.hex()}")
        
        print("Loading...")
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        
        print(f"Status: {tx_receipt.status}")
        print(f"Contract Address: {tx_receipt.contractAddress}")
        
        if tx_receipt.status == 0:
            if tx_receipt.contractAddress:
                return tx_receipt.contractAddress, tx_hash.hex()
            return None, None
        
        return tx_receipt.contractAddress, tx_hash.hex()
        
    except Exception as e:
        print(f"Error detail: {e}")
        return None, None

def format_timestamp():
    now = datetime.now()
    return now.strftime("%H:%M %d-%m-%Y")

def print_center(text):
    """Print teks di tengah dengan lebar 70 karakter"""
    width = 70
    clean = text
    for code in [BLUE, GREEN, YELLOW, RED, RESET, BOLD]:
        clean = clean.replace(code, '')
    padding = max(0, (width - len(clean)) // 2)
    print(f"{' ' * padding}{text}")

def print_line():
    """Print garis pemisah"""
    print("-" * 70)

def main():
    # Menu bahasa
    print(f"\n{BLUE}[1]{RESET} Inggris")
    print(f"{BLUE}[2]{RESET} Bahasa Indonesia")
    print(f"Pilih/Select {BLUE}[1]{RESET} atau/or {BLUE}[2]{RESET}: ")
    
    lang_choice = input().strip()
    
    if lang_choice == "2":
        # Indonesia
        os.system('clear')
        print("\n")
        print_center(f"{BLUE}══════════════════════════════════════════════════════════{RESET}")
        print_center(f"{BLUE}= CHARITO ={RESET}")
        print_center(f"{GREEN}BOT ini di buat oleh Charito individual Developer{RESET}")
        print_center(f"{GREEN}untuk mempermudah membuat Contract Address GIWA Testnet.{RESET}")
        print_center(f"= DUKUNGAN ={RESET}")
        print_center(f"BITCOIN {RED}bc1pvp6dt5v4k5lfyhldfuravqg3zrzvl7t2mkw4n72tae70235q6cyqh44tg2{RESET}")
        print_center(f"ETH,BNB,POL,USDT/USDC,EVM {RED}0xdA8b413B23D20601e8aF7278B5798b26999Ce762{RESET}")
        print_center(f"SOLANA {RED}4yPrmba7d38VXfJyyXeWtbTsVJdNcNYp3BuYKjkk3G9x{RESET}")
        print_center(f"TRON {RED}TEyJgHsVnbKjU7wVkrCo6RAJg8rzLCJF81{RESET}")
        print_center(f"{BLUE}══════════════════════════════════════════════════════════{RESET}")
        print(f"\n{GREEN}Mulai? [Y] or [N]:{RESET} ", end="")
        
        start = input().strip().upper()
        
        if start == "Y":
            print(f"\n{BLUE}Membuat Contract Address :{RESET}")
            print_line()
            
            counter = 1
            while True:
                try:
                    timestamp = format_timestamp()
                    address, hash_tx = create_contract()
                    
                    print(f"\n{BLUE}[ {counter:02d} ]{RESET}")
                    print(f"[{timestamp}]")
                    print(f"{GREEN}Contract Address:{RESET} {address}")
                    print(f"{GREEN}Hash:{RESET} {hash_tx}")
                    print_line()
                    
                    counter += 1
                    time.sleep(3)
                    
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    time.sleep(3)
                    continue
    
    else:
        # Inggris
        os.system('clear')
        print("\n")
        print_center(f"{BLUE}══════════════════════════════════════════════════════════{RESET}")
        print_center(f"{BLUE}= CHARITO ={RESET}")
        print_center(f"{GREEN}This BOT is made by Charito individual Developer{RESET}")
        print_center(f"{GREEN}to make it easier to create Contract Address GIWA Testnet.{RESET}")
        print_center(f"= SUPPORT ={RESET}")
        print_center(f"BITCOIN {RED}bc1pvp6dt5v4k5lfyhldfuravqg3zrzvl7t2mkw4n72tae70235q6cyqh44tg2{RESET}")
        print_center(f"ETH,BNB,POL,USDT/USDC,EVM {RED}0xdA8b413B23D20601e8aF7278B5798b26999Ce762{RESET}")
        print_center(f"SOLANA {RED}4yPrmba7d38VXfJyyXeWtbTsVJdNcNYp3BuYKjkk3G9x{RESET}")
        print_center(f"TRON {RED}TEyJgHsVnbKjU7wVkrCo6RAJg8rzLCJF81{RESET}")
        print_center(f"{BLUE}══════════════════════════════════════════════════════════{RESET}")
        print(f"\n{GREEN}Start? [Y] or [N]:{RESET} ", end="")
        
        start = input().strip().upper()
        
        if start == "Y":
            print(f"\n{BLUE}Create Contract Address :{RESET}")
            print_line()
            
            counter = 1
            while True:
                try:
                    timestamp = format_timestamp()
                    address, hash_tx = create_contract()
                    
                    print(f"\n{BLUE}[ {counter:02d} ]{RESET}")
                    print(f"[{timestamp}]")
                    print(f"{GREEN}Contract Address:{RESET} {address}")
                    print(f"{GREEN}Hash:{RESET} {hash_tx}")
                    print_line()
                    
                    counter += 1
                    time.sleep(3)
                    
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    time.sleep(3)
                    continue

if __name__ == "__main__":
    main()
