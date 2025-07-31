<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Crea tu cuenta</h2>
      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Nombre</label>
          <input
            v-model="form.nombre"
            type="text"
            placeholder="Nombre completo"
            class="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-purple-400 transition"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Correo electrónico</label>
          <input
            v-model="form.email"
            type="email"
            placeholder="correo@ejemplo.com"
            class="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-purple-400 transition"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Contraseña</label>
          <input
            v-model="form.password"
            type="password"
            placeholder="••••••••"
            class="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-purple-400 transition"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-gradient-to-r from-purple-600 to-blue-500 hover:from-purple-500 hover:to-blue-400 text-white py-3 rounded-xl font-semibold hover:scale-[1.02] transition-transform shadow-md"
        >
          Registrarse
        </button>
      </form>

      <router-link to="/" class="block text-center text-blue-600 mt-5 hover:underline">
        ¿Ya tienes cuenta? Inicia sesión
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({ email: '', password: '' })

const handleRegister = async () => {
  try {
    const res = await axios.post('http://localhost:8000/login', form.value)
    alert('Sesión iniciada. Token: ' + res.data.token)
    localStorage.setItem('token', res.data.token)
  } catch (err) {
    alert('Error de autenticación')
  }
}
</script>

<style scoped>
.login-container {
  background: url('/bg-pattern.png') center/cover no-repeat fixed;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

/* Card con efecto glassmorphism */
.login-card {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 20px;
  padding: 2rem;
  width: 100%;
  max-width: 420px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  color: #f1f5f9;
  border: 1px solid rgba(255, 255, 255, 0.1);
  animation: fadeIn 0.8s ease;
}

.login-card h2 {
  text-align: center;
  font-size: 1.75rem;
  margin-bottom: 1.5rem;
  color: #f9fafb;
}

.login-card form {
  display: flex;
  flex-direction: column;
}

.login-card label {
  margin-bottom: 0.25rem;
  font-weight: 500;
  color: #e0e7ff;
}

.login-card input {
  padding: 0.75rem;
  border: none;
  border-radius: 10px;
  margin-bottom: 1rem;
  font-size: 1rem;
  background-color: rgba(255, 255, 255, 0.1);
  color: #f8fafc;
}

.login-card input::placeholder {
  color: #cbd5e1;
}

.login-card input:focus {
  outline: 2px solid #60a5fa;
  background-color: rgba(255, 255, 255, 0.15);
}

.login-card button {
  background: linear-gradient(to right, #3b82f6, #8b5cf6);
  color: white;
  padding: 0.75rem;
  font-weight: bold;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.login-card button:hover {
  transform: scale(1.02);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
}

.register-link {
  display: block;
  text-align: center;
  margin-top: 1.2rem;
  color: #93c5fd;
  font-size: 0.95rem;
  text-decoration: none;
}

.register-link:hover {
  text-decoration: underline;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
