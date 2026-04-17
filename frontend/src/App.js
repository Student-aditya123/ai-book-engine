import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Ask from "./pages/Ask";

function App() {
  return (
    <div>
      <Navbar />
      <Home />
      <Ask />
    </div>
  );
}
export default App;


// import React from "react";
// import Navbar from "./components/Navbar";
// import Home from "./pages/Home";
// import Ask from "./pages/Ask";

// function App() {
//   return (
//     <div>
//       {/* Navbar */}
//       <div className="bg-gray-900 text-white p-4 flex justify-between">
//         <h1 className="font-bold">📚 AI Book Engine</h1>
//         <div>
//           <span className="mr-4">Home</span>
//           <span>Ask AI</span>
//         </div>
//       </div>

//       {/* Pages */}
//       <Home />
//       <Ask />
//     </div>
//   );
// }

// export default App;