
import React, { useState } from 'react';
import './App.css';
  
const App = () => {
  const [isStreaming, setIsStreaming] = useState(true);

  // Assuming your Flask backend provides a continuous .mjpeg stream
  const streamSrc = isStreaming ? 'http://127.0.0.1:5000/video_feed' : '';

  const handleToggleStreaming = () => {
    setIsStreaming(!isStreaming);
  };

  return (
    <div className="app">
      <header className="header">
        Virtual AI Board
      </header>

      <div className="video-container">
        {isStreaming ? (
          <img src={streamSrc} alt="Video Feed" />
        ) : (
          <div className="video-placeholder">Stream Paused</div>
        )}
      </div>

      <div className="controls">
        <button onClick={handleToggleStreaming} className={isStreaming ? 'pause' : 'resume'}>
          {isStreaming ? 'Pause' : 'Resume'}
        </button>
      </div>
    </div>
  );
};


export default App;
