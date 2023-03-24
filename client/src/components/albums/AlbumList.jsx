import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const AlbumList = () => {
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    axios.get('/albums/').then((res) => {
      setAlbums(res.data);
    });
  }, []);

  return (
    <div>
      <h1>Album List</h1>
      <ul>
        {albums.map((album) => (
          <li key={album.int}>
            <Link to={`/albums/${album.pk}`}>{album.name}</Link>
          </li>
        ))}
      </ul>
      <Link to='/albums/create'>Add New Album</Link>
    </div>
  );
};

export default AlbumList;
