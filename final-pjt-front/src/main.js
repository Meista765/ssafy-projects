// Vue.js
import App from './App.vue'; // 루트 컴포넌트
import { createApp } from 'vue'; // Vue 3 앱 생성

// Pinia
import { createPinia } from 'pinia'; // Pinia 상태 관리
import piniaPersistedState from 'pinia-plugin-persistedstate'; // Pinia 상태 유지 플러그인

// Vuetify
import { createVuetify } from 'vuetify'; // Vuetify 프레임워크
import { aliases, mdi } from 'vuetify/lib/iconsets/mdi'; // Material Design Icons
import 'vuetify/styles'; // Vuetify 스타일
import '@mdi/font/css/materialdesignicons.css'; // Material Design Icons CSS

// Vuetify 설정
const vuetify = createVuetify({
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: { mdi },
  },
  theme: {
    defaultTheme: 'light', // 기본 테마 설정 (light/dark)
    themes: {
      light: {
        colors: {
          primary: '#1976D2', // 기본 primary 색상
          secondary: '#424242', // 기본 secondary 색상
        },
      },
    },
  },
});

// Pinia 설정
const pinia = createPinia();
pinia.use(piniaPersistedState); // Pinia에 플러그인 적용

// Vue 앱 생성 및 마운트
const app = createApp(App);
app.use(pinia); // Pinia 사용
app.use(vuetify); // Vuetify 사용
app.mount('#app'); // 앱 마운트
