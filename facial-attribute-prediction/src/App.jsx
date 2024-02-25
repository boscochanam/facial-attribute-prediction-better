import { useState, useEffect } from 'react'
import './App.css'
import ImageDisplay from './components/ImageDisplay'
import Header from './components/Header'

function App() {

  const [time, setTime] = useState(0)

  useEffect(() => {
    fetch('http://127.0.0.1:5000/time').then(res => res.json()).then(data => {
      setTime(data.time)
    })
  }, [])

  return (
    <>
      <Header />
      <ImageDisplay />
      <p>The current time is {time}.</p>
    </>
  )
}

export default App
