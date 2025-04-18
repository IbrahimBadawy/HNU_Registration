<!-- 📁 frontend/src/views/admin/AdminLogin.vue -->
<template>
    <div class="login-container">
      <h2>تسجيل دخول الأدمن</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" placeholder="اسم المستخدم" required />
        <input v-model="password" type="password" placeholder="كلمة المرور" required />
        <button type="submit">دخول</button>
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
      if (!res.data.is_admin) {
        error.value = 'هذا الحساب غير مصرح له بالدخول كأدمن'
        return
      }
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
      localStorage.setItem('is_admin', true)
      router.push('/admin')
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
    background-color: #444;
    color: white;
    border: none;
    cursor: pointer;
  }
  .error {
    color: red;
  }
  </style>
  
