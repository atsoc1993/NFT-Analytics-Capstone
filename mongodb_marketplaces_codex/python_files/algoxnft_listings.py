from algokit_utils import AlgorandClient
from algosdk.transaction import LogicSigAccount
from base64 import b64decode
import json

algorand = AlgorandClient.mainnet()
indexer = algorand.client.indexer

algoxnft_address = 'XNFT36FUCFRR6CK675FW4BEBCCCOJ4HOSMGCN6J2W6ZMB34KM2ENTNQCP4'

log_path = 'algoxnft_sales.jsonl'

def get_txs(next_page=None):
    req = indexer.search_transactions_by_address(address=algoxnft_address, next_page=next_page, sig_type='lsig')
    return req['transactions'], req['next-token']

def check_if_listing_fulfilled(logic_sig_address):
    req = indexer.search_transactions_by_address(logic_sig_address)
    return req['transactions']

def write_sale(record: dict):
    with open(log_path, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(record) + '\n')  


last_page = 'bNxrAQAAAAAYAAAA'
txs, next_page = get_txs(next_page=last_page)

while next_page:
    for tx in txs:
        logic_sig = tx['signature'].get('logicsig', {}).get('logic', None)
        if logic_sig:
            logic_sig_program_bytes = b64decode(logic_sig)
            logic_sig_account_address = LogicSigAccount(program=logic_sig_program_bytes).address()

            disassembled = algorand.client.algod.disassemble(logic_sig_program_bytes)['result'].split('\n')
            found_lister = False
            found_algo_amount = False
            lister = None
            for i, dis in enumerate(disassembled):
                if dis == 'gtxn 3 Receiver':
                    lister = disassembled[i + 1].split(' ')[-1]
                    found_lister = True
                
                if dis == 'gtxn 3 Amount':
                    algo_amount = disassembled[i + 1].split(' ')[-1]
                    found_algo_amount = True
                
                if found_lister and found_algo_amount:
                    break

            logic_sig_txns = check_if_listing_fulfilled(logic_sig_address=logic_sig_account_address)
            asset_sold = False
            for txn in logic_sig_txns:
                asset_transfer = txn.get('asset-transfer-transaction', None)
                if asset_transfer:
                    sender = tx['sender']
                    receiver = asset_transfer['receiver']
                    if lister == None:
                        break
                    if sender == logic_sig_account_address and receiver != lister and receiver != logic_sig_account_address and 'close-to' not in asset_transfer:
                        time = txn['round-time']
                        txn_id = txn['id']
                        asset_sold = True
                        asset_id = asset_transfer['asset-id']
                        record = {
                            "lister"    : lister,
                            "asset_id"  : asset_id,
                            "algo_amt"  : algo_amount,
                            "buyer"     : receiver,
                            "timestamp" : txn['round-time'],
                            "tx_id"     : txn['id']
                        }
                        write_sale(record)
                        print(record)    
                        break

    txs, next_page = get_txs(next_page)
    print(f'Next Page: {next_page}')
    algorand = AlgorandClient.mainnet()
    indexer = algorand.client.indexer
