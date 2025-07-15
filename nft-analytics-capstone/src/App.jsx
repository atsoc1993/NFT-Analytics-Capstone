import { useEffect } from "react"

function App() {

  useEffect(() => {
    testEndpoint();
  }, [])
  
  const testEndpoint = async () => {
    let response = await fetch('http://localhost:3000/get-assets/1')
    console.log(response)
  }

  return (
    <div>Test</div>
  )
}

export default App;