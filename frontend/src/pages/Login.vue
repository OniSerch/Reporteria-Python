<template>
  <div class="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-[#0e101c] via-[#1a1c29] to-[#0e101c] overflow-hidden">

    <!-- Fondo con imagen nebulosa -->
    <div class="absolute inset-0 bg-[url('/nebula.png')] bg-cover opacity-20 blur-sm"></div>

    <!-- Panel central tipo vidrio -->
    <div class="relative bg-white/10 backdrop-blur-xl p-10 rounded-3xl border border-white/10 shadow-[0_0_40px_#8b5cf690] w-full max-w-md z-10">
      <h2 class="text-3xl font-bold text-white text-center mb-6">Iniciar sesión</h2>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <input
          v-model="form.email"
          type="email"
          placeholder="Correo electrónico"
          class="w-full p-3 rounded-xl bg-white/5 border border-white/20 text-white placeholder:text-white/40 focus:outline-none focus:ring-2 focus:ring-cyan-400 transition"
        />

        <input
          v-model="form.password"
          type="password"
          placeholder="Contraseña"
          class="w-full p-3 rounded-xl bg-white/5 border border-white/20 text-white placeholder:text-white/40 focus:outline-none focus:ring-2 focus:ring-purple-500 transition"
        />

        <button
          type="submit"
          class="w-full bg-gradient-to-r from-purple-600 to-blue-500 hover:from-purple-500 hover:to-cyan-400 text-white py-3 rounded-xl font-bold hover:scale-105 transition-transform shadow-lg"
        >
          Entrar
        </button>
      </form>

      <router-link to="/register" class="block text-center text-cyan-300 mt-4 hover:underline">
        ¿No tienes cuenta? Regístrate
      </router-link>
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
