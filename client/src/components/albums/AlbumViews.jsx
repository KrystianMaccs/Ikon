import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AlbumsSerializer from '../albums/AlbumsSerializer';



const AlbumViews = () => {
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get('/albums/');
        setAlbums(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, []);

  const createAlbum = async (albumData) => {
    try {
      const res = await axios.post('/albums/', albumData);
      setAlbums([...albums, res.data]);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Albums</h2>
      <AlbumsSerializer albums={albums} createAlbum={createAlbum} />
    </div>
  );
};

export default AlbumViews;
