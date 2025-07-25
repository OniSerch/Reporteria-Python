<template>
  <div class="p-6 max-w-md mx-auto">
    <h2 class="text-2xl font-bold mb-4">Iniciar Sesión</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="form.email" placeholder="Correo" class="border p-2 w-full mb-2" />
      <input v-model="form.password" type="password" placeholder="Contraseña" class="border p-2 w-full mb-2" />
      <button class="bg-green-600 text-white px-4 py-2">Entrar</button>
    </form>
    <router-link to="/register" class="text-blue-600 mt-4 block">¿No tienes cuenta? Regístrate</router-link>
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
