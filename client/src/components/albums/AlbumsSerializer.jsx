import React, { useState } from 'react';

const AlbumsSerializer = ({ albums, createAlbum }) => {
  const [formData, setFormData] = useState({ title: '', description: '' });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    createAlbum(formData);
    setFormData({ title: '', description: '' });
  };

  return (
    <>
      <ul>
        {albums.map((album) => (
          <li key={album.id}>
            <h3>{album.title}</h3>
            <p>{album.description}</p>
          </li>
        ))}
      </ul>
      <form onSubmit={handleSubmit}>
        <input type="text" name="title" value={formData.title} placeholder="Title" onChange={handleChange} />
        <br />
        <textarea name="description" value={formData.description} placeholder="Description" onChange={handleChange} />
        <br />
        <button type="submit">Create Album</button>
      </form>
    </>
  );
};

export default AlbumsSerializer;
