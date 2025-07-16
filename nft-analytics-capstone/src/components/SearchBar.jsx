import { useState } from 'react';
import './SearchBar.css'

export default function SearchBar() {

    const [searchResults, setSearchResults] = useState([])

    const getNFTs = async (e) => {
        let response = await fetch(`http://localhost:3000/get-assets/${e.target.value}`)
        let data = await response.json();
        console.log(data);
    }
    return (
        <div className="searchbar-div">
            <input onChange={(e) => getNFTs(e)} placeholder="Asset ID or Asset Name"></input>
            {searchResults.map((result) => (
                <div key={result}>
                </div>
            ))}
        </div>
    )
}