import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [merch, setMerch] = useState([])

  async function fetchMerch() {
    const response = await fetch('http://localhost:8000/api/merchandises/')
    const data = await response.json()
    setMerch(data)
  }

  useEffect(() => {
    fetchMerch()
  }, [])

  return (
    <div>
      {merch.map(item => (
        <div key={item.id} className="merch-item">
          <h3>{item.name}</h3>
          <img src={item.image} alt={item.name} />
        </div>
      ))}
    </div>
  )
}

export default App
