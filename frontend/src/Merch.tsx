import { useParams } from "react-router";
import { useState, useEffect } from "react";

function Merch() {
  const { id } = useParams<{ id: string }>()
  const [merch, setMerch] = useState({})

  async function fetchMerch() {
      const response = await fetch('http://localhost:8000/api/merchandises/')
      const data = await response.json()
      setMerch(data.find(item => item.id == id))
    }
  
    useEffect(() => {
      fetchMerch()
    }, [])

  return (
    
    <div>
      <h1>Merch</h1>
      <p>Welcome to the Merch page! {id}</p>
      <pre>{JSON.stringify(merch)}</pre>
    </div>
  );
}

export default Merch