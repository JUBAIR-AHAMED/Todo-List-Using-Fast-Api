import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Todolist from './pages/Todolist.js';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/mytodo" element={<Todolist />} />
      </Routes>
    </Router>
  );
}