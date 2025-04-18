// 📁 frontend/src/router/index.js

import { createRouter, createWebHistory } from "vue-router";
import Register from "../views/Register.vue";
import Login from "../views/Login.vue";
import ApplicationWizard from "../views/ApplicationWizard.vue";
import TrackStatus from "../views/student/TrackStatus.vue";
import AdminLogin from "../views/admin/AdminLogin.vue";
import AdminDashboard from "../views/admin/AdminDashboard.vue";
import ApplicationDetail from "../views/admin/ApplicationDetail.vue";
import Forbidden from "../views/Forbidden.vue";

const routes = [
  { path: "/", redirect: "/register" },
  { path: "/register", component: Register },
  { path: "/login", component: Login },
  { path: "/application", component: ApplicationWizard },
  { path: "/track", component: TrackStatus },
  { path: "/admin/login", component: AdminLogin },
  { path: "/admin", component: AdminDashboard },
  { path: "/admin/application/:id", component: ApplicationDetail },
  { path: "/forbidden", component: Forbidden },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
