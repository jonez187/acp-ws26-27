import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    // Anfragen an /api werden an das FastAPI-Backend weitergeleitet.
    // Dadurch braucht das Backend in der Entwicklung keine CORS-Konfiguration.
    proxy: {
      '/api': 'http://127.0.0.1:8000',
    },
  },
})
