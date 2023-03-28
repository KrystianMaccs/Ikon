import React, { useState } from 'react';

const PhotosSerializer = ({ photos, albumId, createPhoto, updatePhoto, deletePhoto }) => {
  const [formData, setFormData] = useState({ title: '', description: '', image: null });
  const [editingPhotoId, setEditingPhotoId] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.type === 'file' ? e.target.files[0] : e.target.value });
  };

  const handleEditClick = (photoId) => {
    const photoToEdit = photos.find((photo) => photo.id === photoId);
    setFormData({ title: photoToEdit.title, description: photoToEdit.description, image: null });
    setEditingPhotoId(photoId);
  };

  const handleCancelEditClick = () => {
    setFormData({ title: '', description: '', image: null });
    setEditingPhotoId(null);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (editingPhotoId) {
      updatePhoto(editingPhotoId, formData);
      setFormData({ title: '', description: '', image: null });
      setEditingPhotoId(null);
    } else {
      createPhoto(albumId, formData);
      setFormData({ title: '', description: '', image: null });
    }
  };

  return (
    <>
      <ul>
        {photos.map((photo) => (
          <li key={photo.id}>
            <h3>{photo.title}</h3>
            <p>{photo.description}</p>
            <img src={photo.image} alt={photo.title} />
            <button type="button" onClick={() => handleEditClick(photo.id)}>
              Edit
            </button>
            <button type="button" onClick={() => deletePhoto(photo.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
      {albumId && (
        <form onSubmit={handleSubmit}>
          <input type="text" name="title" value={formData.title} placeholder="Title" onChange={handleChange} />
          <br />
          <textarea name="description" value={formData.description} placeholder="Description" onChange={handleChange} />
          <br />
          <input type="file" name="image" accept="image/*" onChange={handleChange} />
          <br />
          <button type="submit">{editingPhotoId ? 'Update' : 'Create'}</button>
          {editingPhotoId && (
            <button type="button" onClick={handleCancelEditClick}>
              Cancel
            </button>
          )}
        </form>
      )}
    </>
  );
};

export default PhotosSerializer;
