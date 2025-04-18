<!-- 📁 frontend/src/views/Login.vue -->
<template>
    <div class="login-container">
      <h2>تسجيل دخول الطالب</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" placeholder="اسم المستخدم" required />
        <input v-model="password" type="password" placeholder="كلمة المرور" required />
        <button type="submit">تسجيل الدخول</button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const password = ref('')
  const error = ref('')
  const router = useRouter()
  
  const handleLogin = async () => {
    try {
      const res = await axios.post('/api/token/', {
        username: username.value,
        password: password.value
      })
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
      router.push('/application')
    } catch (err) {
      error.value = 'بيانات الدخول غير صحيحة'
    }
  }
  </script>
  
  <style scoped>
  .login-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  input, button {
    padding: 10px;
    font-size: 1rem;
  }
  button {
    background-color: #1976d2;
    color: white;
    border: none;
    cursor: pointer;
  }
  .error {
    color: red;
  }
  </style>
