<template>
    <div class="forbidden">
      <h1>403 - غير مصرح</h1>
      <p>ليس لديك صلاحية الوصول لهذه الصفحة.</p>
      <router-link to="/">العودة للصفحة الرئيسية</router-link>
    </div>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  .forbidden {
    text-align: center;
    padding: 80px;
    font-family: 'Cairo', sans-serif;
  }
  h1 {
    font-size: 3rem;
    color: #d32f2f;
  }
  p {
    font-size: 1.2rem;
    margin: 20px 0;
  }
  a {
    color: #1976d2;
    font-weight: bold;
    text-decoration: none;
  }
  </style>