<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Iniciar sesión</h2>

      <form @submit.prevent="handleLogin">
        <label for="email">Correo electrónico</label>
        <input type="email" id="email" v-model="form.email" placeholder="usuario@empresa.com" />

        <label for="password">Contraseña</label>
        <input type="password" id="password" v-model="form.password" placeholder="••••••••" />

        <button type="submit">Entrar</button>
      </form>

      <router-link to="/register" class="register-link">¿No tienes cuenta? Regístrate</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({ email: '', password: '' })

const handleLogin = async () => {
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
