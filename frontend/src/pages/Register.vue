<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-100 to-gray-300 px-4">
    <div class="w-full max-w-md bg-white/70 backdrop-blur-lg rounded-2xl shadow-xl p-8 border border-white/40">

      <h2 class="text-2xl font-bold text-gray-800 text-center mb-6">Crea tu cuenta</h2>

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
