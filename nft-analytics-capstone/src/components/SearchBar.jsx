import { useState } from 'react';
import './SearchBar.css'

export default function SearchBar({ setInspectingAsset }) {

    const [searchResults, setSearchResults] = useState([])
    const [searched, setSearched] = useState(false);

    const getNFTs = async (e) => {
        if (e.target.value === '') {
            setSearched(false);
            return
        }
        let response = await fetch(`http://localhost:3000/get-assets/${e.target.value}`)
        let data = await response.json();
        setSearchResults(data)
        setSearched(true);
    }

    const clickedADiv = () => {
        setInspectingAsset(true);
    }
    return (
        <div className="searchbar-div">
            <input onChange={(e) => getNFTs(e)} placeholder="Asset ID or Asset Name"></input>
            {searched && <div className='search-result-div'>
                {searchResults.map((result) => (
                    <div onClick={clickedADiv} key={result['asset-id']}>
                        {result['asset-name']}: {result['asset-id']}
                    </div>
                ))}
            </div>
            }
        </div>


    )
}