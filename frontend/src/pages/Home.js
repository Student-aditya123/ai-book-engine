import React, { useEffect, useState } from "react";
import { getBooks } from "../api/api";

function Home() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    getBooks().then((res) => setBooks(res.data));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">📚 Book List</h1>

      <div className="grid md:grid-cols-3 gap-6">
            {books.map((book) => (
              <div
                  key={book.id}
                  className="bg-white/10 backdrop-blur-lg p-5 rounded-2xl shadow-xl hover:scale-105 transition"
                >
               <h2 className="font-bold text-lg text-blue-300">
                 {book.title}
               </h2>

                <p className="text-sm text-gray-300 mt-2">
                    {book.description.slice(0, 120)}...
               </p>

                <a
                   href={book.url}
                   target="_blank"
                   className="text-blue-400 text-sm mt-3 inline-block"
                >
                  View Book →
               </a>
             </div>
          ))}
       </div>
    </div>
  );
}

export default Home;


