<!-- 📁 frontend/src/views/Register.vue -->
<template>
    <div class="register-container">
      <h2>تسجيل حساب جديد</h2>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="اسم المستخدم" required />
        <input v-model="email" type="email" placeholder="البريد الإلكتروني" required />
        <input v-model="password" type="password" placeholder="كلمة المرور" required />
        <button type="submit">تسجيل</button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const email = ref('')
  const password = ref('')
  const error = ref('')
  const router = useRouter()
  
  const register = async () => {
    try {
      await axios.post('/api/register/', {
        username: username.value,
        email: email.value,
        password: password.value
      })
      alert('تم إنشاء الحساب بنجاح')
      router.push('/login')
    } catch (err) {
      error.value = 'فشل في إنشاء الحساب. تأكد من صحة البيانات.'
    }
  }
  </script>
  
  <style scoped>
  .register-container {
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
