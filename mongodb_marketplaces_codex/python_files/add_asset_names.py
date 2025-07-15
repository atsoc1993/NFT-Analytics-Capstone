import json
import time
from algokit_utils import AlgorandClient

with open('mongodb_marketplaces_codex/python_files/algoxnft_sales.jsonl', 'r', encoding='utf-8') as input_file:
    data = [json.loads(line) for line in input_file] 

algorand = AlgorandClient.mainnet()

with open('mongodb_marketplaces_codex/python_files/algoxnft_sales_with_names.jsonl', 'a', encoding='utf-8') as outputfile:
    for i, d in enumerate(data):
        if i >= 11576:
            time.sleep(0.2)
            try:
                asset_name = algorand.asset.get_by_id(int(d['asset_id'])).asset_name
                d['asset-name'] = asset_name
            except:
                d['asset-name'] = '_Destroyed Asset, No Info Available'
            outputfile.write(json.dumps(d) + '\n')
