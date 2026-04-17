import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/api";

export const getBooks = () => axios.get(`${BASE_URL}/books/`);

export const askAI = (question) =>
  axios.post(`${BASE_URL}/ask/`, { question });