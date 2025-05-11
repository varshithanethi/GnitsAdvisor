import React from 'react';
import Chatbot from './components/Chatbot';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>GNITS FAQ Assistant</h1>
      </header>
      <main>
        <Chatbot />
      </main>
    </div>
  );
}

export default App;
