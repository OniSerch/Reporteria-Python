<template>
  <div>
    <h2>Sube tu archivo</h2>
    <input type="file" @change="handleFile" />
    <button @click="analizar">Analizar</button>

    <div v-if="resultado">
      <h3>Resultado:</h3>
      <pre>{{ resultado }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const archivo = ref(null)
const resultado = ref(null)

function handleFile(e) {
  archivo.value = e.target.files[0]
}

async function analizar() {
  const formData = new FormData()
  formData.append("file", archivo.value)

  const res = await axios.post("http://localhost:8000/analizar", formData)
  resultado.value = res.data
}
</script>
