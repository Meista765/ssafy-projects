// Vue core
import { createApp } from 'vue'
import App from './App.vue'

// Router
import router from './router'

// Pinia
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// Vuetify
import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Vuetify 설정
const vuetify = createVuetify({
  components,
  directives,
})

// 앱 초기화 및 플러그인 설정
const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

// 플러그인 사용
app.use(pinia)
app.use(router)
app.use(vuetify)

// 앱 마운트
app.mount('#app')