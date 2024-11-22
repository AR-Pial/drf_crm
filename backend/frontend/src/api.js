// src/api.js

const API_URL = process.env.VUE_APP_API_URL || 'http://localhost:8000/api';

export const endpoints = {
  proposals: `${API_URL}/proposals/`,
};
