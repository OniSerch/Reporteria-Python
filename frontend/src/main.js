import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './style.css'   // Tailwind
import './theme.css'   // Personalización visual limpia (si la necesitas)



createApp(App).use(router).mount('#app')
