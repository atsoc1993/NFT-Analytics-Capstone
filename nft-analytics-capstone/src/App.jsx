import { useEffect } from "react"
import Header from './components/Header.jsx'
import SearchBar from "./components/SearchBar";
import { useState } from "react";

function App() {

  const [inspectingAsset, setInspectingAsset] = useState(false);

  return (
    <>
      {!inspectingAsset ?
        <>
          <Header />
          <SearchBar setInspectingAsset={setInspectingAsset} />
        </>
        :
        <div>User is inspecting an asset</div>
      }
    </>

  )
}

export default App;