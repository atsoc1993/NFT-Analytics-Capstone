import json
import time
from algokit_utils import AlgorandClient

with open('mongodb_marketplaces_codex/python_files/algoxnft_sales_with_names.jsonl', 'r', encoding='utf-8') as input_file:
    data = [json.loads(line) for line in input_file] 

algorand = AlgorandClient.mainnet()

# {"lister": "QI2SFEIH3H3CT2NSUMYKDWTKYTKDTM3AQ574V3UE2NYDW2PDSBT4WNGVAA", 
# "asset_id": 435767591, 
# "algo_amt": "22375000", 
# "buyer": "HFEPPHD62GE7HI52TDLGV2IK5UVT6EMJ5INE725JXWRRAHFG6UELLHG3SU", 
# "timestamp": 1641980689, 
# "tx_id": "E77JY6PNLQTHNQOEPSWXKLPANNL57JHV7DPYKY3CGHBZY76FZ7OA", 
# "asset-name": "samuraivia #48"}

# new format will be :
'''
    { asset_id, asset_name, sales: [{lister, buyer, algoamt, tx_id, timestamp}[]]}

'''
complete_data = {}
for d in data:
    key = d['asset_id']
    if key not in complete_data:
        obj = { 
            'asset-id': d['asset_id'],
            'asset-name': d['asset-name'],
            'sales': [
                {
                    'lister': d['lister'],
                    'buyer': d['buyer'],
                    'algo-amt': d['algo_amt'],
                    'tx-id': d['tx_id'],
                    'timestamp': d['timestamp']

                }
            ]
        }
        complete_data[key] = obj
    else:
        inner_obj = {
            'lister': d['lister'],
            'buyer': d['buyer'],
            'algo-amt': d['algo_amt'],
            'tx-id': d['tx_id'],
            'timestamp': d['timestamp']

        }
        complete_data[key]['sales'].append(inner_obj)

# for _ in complete_data:
#     print(_, complete_data[_])
with open('mongodb_marketplaces_codex/python_files/algoxnft_sales_with_names_and_consolidated.jsonl', 'w', encoding='utf-8') as outputfile:
    for _ in complete_data:
        print(_, complete_data[_])
        outputfile.write(json.dumps(complete_data[_]) + '\n')
