import React from 'react'
import { BrowserRouter } from 'react-router-dom'
import AddAlbum from './components/albums/AddAlbum'
import AlbumList from './components/albums/AlbumList'
import AlbumDetail from './components/albums/AlbumDetail'
import PhotoDetail from './components/photos/PhotoDetail'

const Greet = () => {
  return (
    <div>Greet. This is a simple greet component</div>
  )
}


function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <AlbumList />
        <AddAlbum />
        <AlbumDetail />
        <PhotoDetail />
      </BrowserRouter>

     
      <Greet />
    </div>
  )
}

export default App
