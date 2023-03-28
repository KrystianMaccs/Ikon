import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { BrowserRouter as Router, Link } from 'react-router-dom';
import AlbumViews from './components/albums/AlbumViews';
import PhotosView from './components/photos/PhotosView';

const Apps = () => {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/albums">Albums</Link>
          </li>
          <li>
            <Link to="/photos">Photos</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/albums" element={<AlbumViews />} />
        <Route path="/photos" element={<PhotosView />} />
      </Routes>
    </Router>
  );
};

export default Apps;
