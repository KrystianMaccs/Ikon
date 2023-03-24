import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const PhotoDetail = () => {
  const [photo, setPhoto] = useState(null);
  const { albumId, photoId } = useParams();

  useEffect(() => {
    axios.get(`/albums/${albumId}/photos/${photoId}`).then((res) => {
      setPhoto(res.data);
    });
  }, [albumId, photoId]);

  if (!photo) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{photo.name}</h1>
      <img src={photo.image} alt={photo.name} />
      <p>{photo.description}</p>
    </div>
  );
};

export default PhotoDetail;
