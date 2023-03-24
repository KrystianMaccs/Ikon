import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link, useParams } from 'react-router-dom';

const AlbumDetail = () => {
  const [album, setAlbum] = useState(null);
  const { albumId } = useParams();

  useEffect(() => {
    axios.get(`/albums/${albumId}`).then((res) => {
      setAlbum(res.data);
    });
  }, [albumId]);

  if (!album) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{album.name}</h1>
      <p>{album.description}</p>
      <ul>
        {album.photos.map((photo) => (
          <li key={photo.pk}>
            <Link to={`/albums/${album.pk}/photos/${photo.pk}`}>{photo.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AlbumDetail;
