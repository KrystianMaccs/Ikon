import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const AddAlbum = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: '',
    description: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/albums/', formData)
      .then((res) => {
        console.log(res.data);
        // redirect to album detail page
        navigate(`/albums/${res.data.pk}`);
      })
      .catch((error) => {
        if (error.response && error.response.status === 404) {
          console.log("Resource not found");
          // handle the error gracefully
        } else {
          console.log("An error occurred");
          // handle other errors
        }
      });
  };
  

  return (
    <div>
      <h1>Add New Album</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor='name'>Name:</label>
        <input type='text' name='name' onChange={handleChange} value={formData.name} />
        <label htmlFor='description'>Description:</label>
        <textarea name='description' onChange={handleChange} value={formData.description}></textarea>
        <button type='submit'>Add Album</button>
      </form>
    </div>
  );
};

export default AddAlbum;
