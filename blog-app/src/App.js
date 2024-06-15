import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PostList from './components/PostList';
import CreatePost from './components/CreatePost';
import API_URL from './config'

const App = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch(`${API_URL}/get-items`); // Replace with your actual API endpoint
        if (response.ok) {
          const data = await response.json();
          setPosts(data); // Update state with fetched data
        } else {
          console.error('Failed to fetch posts');
        }
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    };

    fetchPosts();
  }, []); // Empty dependency array ensures this effect runs only once on mount

  const addPost = (post) => {
    setPosts([...posts, post]);
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<PostList posts={posts} />} />
        <Route path="/create-post" element={<CreatePost addPost={addPost} />} />
      </Routes>
    </Router>
  );
};

export default App;
