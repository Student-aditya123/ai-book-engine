import React from "react";

function Navbar() {
  return (
    <div className="flex justify-between items-center px-8 py-4 bg-black/30 backdrop-blur-md shadow-lg">
      <h1 className="text-xl font-bold text-blue-400">
        🚀 AI Book Engine
      </h1>
      <p className="text-sm text-gray-300">Powered by RAG + AI</p>
    </div>
  );
}

export default Navbar;