import json


with open('algoxnft_sales.jsonl', 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f] 

top_10_sales = []
for d in data:
    algo_amt = int(d['algo_amt'])
    asset_id = d['asset_id']

    if len(top_10_sales) < 10:
        top_10_sales.append((algo_amt, asset_id))
    
    else:

        lowest_priced_item = None
        lowest_price_item_index = None
        for i, item in enumerate(top_10_sales):
            if lowest_priced_item == None:
                lowest_priced_item = item[0]
                lowest_price_item_index = i
            else:
                if item[0] < lowest_priced_item:
                    lowest_priced_item = item[0]
                    lowest_price_item_index = i

        if algo_amt > lowest_priced_item:
            top_10_sales[lowest_price_item_index] = (algo_amt, asset_id)


top_10_sales.sort(reverse=True)

for sale in top_10_sales:
    print(sale[0] / 10**6, sale[1])
