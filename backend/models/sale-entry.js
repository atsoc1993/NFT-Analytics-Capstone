import mongoose from "mongoose";
import dotenv from 'dotenv'

dotenv.config({ path: '../.env'})

// // keys are lister, asset_id, algo_amt, buyer, timestamp & tx_id
const DB_ACCESS_URI = process.env.DB_ACCESS_URI


const SaleType = mongoose.Schema({
    'algo-amt': {
        type: Number,
        required: true
    },
    'lister': {
        type: String,
        required: true
    },
    'buyer': {
        type: String,
        required: true
    },
    'tx-id': {
        type: String,
        required: true
    },
    'timestamp': {
        type: Number,
        required: true
    }
})

try {
    console.log("Connecting")
    await mongoose.connect(DB_ACCESS_URI)
    console.log("Connected")

} catch (e) {
    console.log(e)
}
let SaleSchema = mongoose.Schema({
    'asset-id': {
        type: String,
        required: true
    },
    'asset-name': {
        type: String,
        required: true
    },
    'sales': {
        type: [SaleType],
        required: true,
    }

})

export default mongoose.model('Sale', SaleSchema)