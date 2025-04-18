// 📁 frontend/vite.config.js
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path"; // 👈 مهم جداً

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"), // 👈 حل مشكلة @
    },
  },
  server: {
    proxy: {
      "/api": "http://localhost:8000", // Django server
    },
  },
});
