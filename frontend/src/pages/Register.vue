<template>
  <div class="p-6 max-w-md mx-auto">
    <h2 class="text-2xl font-bold mb-4">Registro</h2>
    <form @submit.prevent="handleRegister">
      <input v-model="form.nombre" placeholder="Nombre" class="border p-2 w-full mb-2" />
      <input v-model="form.email" placeholder="Correo" class="border p-2 w-full mb-2" />
      <input v-model="form.password" type="password" placeholder="Contraseña" class="border p-2 w-full mb-2" />
      <button class="bg-blue-600 text-white px-4 py-2">Registrarse</button>
    </form>
    <router-link to="/" class="text-blue-600 mt-4 block">¿Ya tienes cuenta? Inicia sesión</router-link>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({ nombre: '', email: '', password: '' })

const handleRegister = async () => {
  try {
    await axios.post('http://localhost:8000/register', form.value)
    alert('Registro exitoso')
  } catch (err) {
    alert('Error al registrar')
  }
}
</script>
