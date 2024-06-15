import React from 'react';
import { Link } from 'react-router-dom';

const PostList = ({ posts }) => {
  return (
    <div>
      <h1>All Posts</h1>
      <Link to="/create-post">
        <button style={{ float: 'right' }}>Create Post</button>
      </Link>
      {posts.map((post, index) => (
        <div key={index} style={{ border: '1px solid black', margin: '10px', padding: '10px' }}>
          <h2>{post.title}</h2>
          <img src={post.image} alt={post.title} style={{ maxWidth: '100%' }} />
          <p>{post.content}</p>
        </div>
      ))}
    </div>
  );
};

export default PostList;
