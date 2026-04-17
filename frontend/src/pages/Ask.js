import React, { useState } from "react";
import { askAI } from "../api/api";

function Ask() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    setLoading(true);
    const res = await askAI(question);
    setAnswer(res.data.answer);
    setLoading(false);
  };

  return (
         <div className="p-6 max-w-2xl mx-auto">
              <h1 className="text-2xl font-bold mb-4 text-center">
                  🤖 Ask AI About Books
             </h1>

             <div className="bg-blue-900/50 backdrop-blur-md p-4 rounded-xl shadow-lg">
                 <input
                       className="w-full p-3 rounded bg-black/40 border border-gray-600 text-white"
                       placeholder="Ask something like: Recommend similar books..."
                       value={question}
                       onChange={(e) => setQuestion(e.target.value)}
                   />

                  <button
                        onClick={handleAsk}
                        className="mt-3 w-full bg-blue-500 hover:bg-blue-600 py-2 rounded"
                   >
                       {loading ? "Thinking..." : "Ask AI 🚀"}
                  </button>
              </div>

              {answer && (
                  <div className="mt-6 bg-white/10 p-4 rounded-xl shadow-lg">
                     <h2 className="font-semibold text-blue-300">AI Response:</h2>
                     <p className="text-gray-200 mt-2">{answer}</p>
                  </div>
               )}
          </div>
      
  );
}

export default Ask;
