// 📁 frontend/src/main.js

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";

import "./style.css"; // لو حابب تضيف تنسيقات عامة

const app = createApp(App);

app.use(router);
app.use(createPinia());
app.mount("#app");
