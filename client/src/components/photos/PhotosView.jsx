import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PhotosSerializer from '../photos/PhotosSerializer';


const PhotosView = ({ albumId }) => {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await axios.get(`/photos/${albumId ? `?album_id=${albumId}` : ''}`);
        setPhotos(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, [albumId]);

  const createPhoto = async (photoData) => {
    try {
      const res = await axios.post(`/photos/${albumId}/`, photoData);
      setPhotos([...photos, res.data]);
    } catch (err) {
      console.error(err);
    }
  };

  const updatePhoto = async (photoId, photoData) => {
    try {
      const res = await axios.put(`/photos/${photoId}/`, photoData);
      const updatedPhotos = photos.map((photo) => (photo.id === res.data.id ? res.data : photo));
      setPhotos(updatedPhotos);
    } catch (err) {
      console.error(err);
    }
  };

  const deletePhoto = async (photoId) => {
    try {
      await axios.delete(`/photos/${photoId}/`);
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