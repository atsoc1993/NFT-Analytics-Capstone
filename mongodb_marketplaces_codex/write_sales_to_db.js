import fs from 'fs'
import mongoose from 'mongoose'
import Sale from '../backend/models/sale-entry.js'
import dotenv from 'dotenv'

dotenv.config({ path: '../.env' })

let data = fs.readFileSync('./algoxnft_sales_with_names.jsonl', 'utf-8')
data = data.split('\n')
data = data.filter(line => line !== '')
data = data.map(line => JSON.parse(line))
// keys are lister, asset_id, algo_amt, buyer, timestamp & tx_id
const DB_ACCESS_URI = process.env.DB_ACCESS_URI
console.log(DB_ACCESS_URI)
try {
    console.log("Connecting")
    await mongoose.connect(DB_ACCESS_URI)
    console.log("Connected")

} catch (e) {
    console.log(e)
}

for (let d of data) {
    let saleObj = {
        'asset-id': String(d['asset_id']),
        'asset-name': d['asset-name'],
        'algo-amt': Number(d['algo_amt']),
        'lister': d['lister'],
        'buyer': d['buyer'],
        'tx-id': d['tx_id'],
        'timestamp': Number(d['timestamp'])
    }

    try {
        await Sale.insertOne(saleObj)

    } catch (e) {
        console.log(e)
    }
}
