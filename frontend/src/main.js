import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'

import 'bootstrap/dist/css/bootstrap.css'
import './assets/main.css'
import 'bootstrap/dist/js/bootstrap.js'

createApp(App).use(router).use(createPinia()).mount('#app')
