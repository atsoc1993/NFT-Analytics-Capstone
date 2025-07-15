import express from 'express'
import cors from 'cors';
import mongoose from 'mongoose';
import dotenv from 'dotenv'
import Sale from './models/sale-entry.js';
dotenv.config({ path: '../.env' })

const app = express();
app.use(cors());

console.log("Connecting to MongoDB")
mongoose.connect(process.env.DB_ACCESS_URI)
console.log("Connected to MongoDB")


app.get('/get-assets/:assetNameOrID', async (req, res) => {
    let chars = req.params.assetNameOrID
    console.log(chars)
    let searchType;
    if (Number(chars)) {
        searchType = 'asset-id'
    } else {
        searchType = 'asset-name'
    }
    console.log(searchType);
    let regexSearchExpr = new RegExp(`^${chars}`, 'i')
    let sales = await Sale.find({ [searchType]: { $regex: regexSearchExpr } })
    console.log(sales)

})

const PORT = 3000

app.listen(PORT, () => {
    console.log(`App running @ http://localhost:${3000}`)
})