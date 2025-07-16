import { useEffect } from "react"
import Header from './components/Header.jsx'

import SearchBar from "./components/SearchBar";
function App() {

  // useEffect(() => {
  //   testEndpoint();
  // }, [])

  // const testEndpoint = async () => {
  //   
  // }

  return (
    <>
    <Header/>
    <SearchBar/>
    </>
  )
}

export default App;