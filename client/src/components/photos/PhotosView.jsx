import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PhotosSerializer from '../photos/PhotosSerializer';


const PhotosView = ({ albumId }) => {
  const [photos, setPhotos] = useState([]);
  const API = "http://127.0.0.1:8000/api/v1/gallery/albums/";
  const authorization = {
    headers: {
      Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMTE0OTkxLCJqdGkiOiJjN2Y5NzY2MDVlZTg0MTg4ODZhN2NiZWE0ODcxNjRiNyIsInVzZXJfaWQiOiI4N2M2MTFhYS0zNTIxLTQzM2EtOWI5Yy1jMTFiNjU5YTJlNTIifQ.6bQdCqgQz_6aRocJe5z9eYB2iEzmpUyC2o_hp9zB64Y`,
    }
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get(API, `/${albumId ? `?album_id=${albumId}` : ''}`);
        setPhotos(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, [albumId]);

  const createPhoto = async (photoData) => {
    try {
      const res = await axios.post(API, `/${albumId}/`, photoData);
      setPhotos([...photos, res.data]);
    } catch (err) {
      console.error(err);
    }
  };

  const updatePhoto = async (photoId, photoData) => {
    try {
      const res = await axios.put(API, authorization, `/${photoId}/`, photoData);
      const updatedPhotos = photos.map((photo) => (photo.id === res.data.id ? res.data : photo));
      setPhotos(updatedPhotos);
    } catch (err) {
      console.error(err);
    }
  };

  const deletePhoto = async (photoId) => {
    try {
      await axios.delete(API, authorization, `/${photoId}/`);
      setPhotos(photos.filter((photo) => photo.id !== photoId));
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Photos</h2>
      <PhotosSerializer
        photos={photos}
        albumId={albumId}
        createPhoto={createPhoto}
        updatePhoto={updatePhoto}
        deletePhoto={deletePhoto}
      />
    </div>
  );
};

export default PhotosView;