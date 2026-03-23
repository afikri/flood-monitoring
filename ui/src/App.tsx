import { useEffect, useState } from 'react'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import axios from 'axios'
import 'leaflet/dist/leaflet.css'

interface Station {
  id: number
  station_id: string
  name: string
  latitude: number
  longitude: number
  alert_threshold: number
}


function App() {
  const [stations, setStations] = useState<Station[]>([])

  
  useEffect(() => {
    // Fetch from Django API
    axios.get('http://127.0.0.1:8000/api/v1/stations/')
      .then(res => setStations(res.data))
      .catch(err => console.error("API Error:", err))
  }, [])

  return (
    <>
      <div style={{ textAlign: 'center', fontFamily: 'sans-serif' }}>
      <h1>🌊 Flood Level Monitoring</h1>
      <p>Demo for Eurac Research (RECEPTIC Role)</p>
      
      <MapContainer 
        center={[5.5, 95.5] as [number, number]} 
        zoom={8} 
        style={{ height: '500px', width: '90%', margin: 'auto' }}
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        
        {stations.map(station => (
          <Marker key={station.id} position={[station.latitude, station.longitude]}>
            <Popup>
              <strong>{station.name}</strong><br/>
              Threshold: {station.alert_threshold}m<br/>
              ID: {station.station_id}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
    </>
  )
}

export default App
