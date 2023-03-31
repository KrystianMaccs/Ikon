import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AlbumsSerializer from '../albums/AlbumsSerializer';



const AlbumViews = () => {
  const [albums, setAlbums] = useState([]);
  const API = "http://127.0.0.1:8000/api/v1/gallery/photos/";
  const authorization = {
    headers: {
      Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMTE0OTkxLCJqdGkiOiJjN2Y5NzY2MDVlZTg0MTg4ODZhN2NiZWE0ODcxNjRiNyIsInVzZXJfaWQiOiI4N2M2MTFhYS0zNTIxLTQzM2EtOWI5Yy1jMTFiNjU5YTJlNTIifQ.6bQdCqgQz_6aRocJe5z9eYB2iEzmpUyC2o_hp9zB64Y`,
    }
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get(API, authorization);
        setAlbums(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, []);

  const createAlbum = async (albumData) => {
    try {
      const res = await axios.post(API, authorization, albumData);
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
