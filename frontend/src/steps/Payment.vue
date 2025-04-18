

<!-- 📁 frontend/src/steps/Payment.vue -->
<template>
    <div class="step">
      <h2>الدفع الإلكتروني</h2>
      <p>اضغط على الزر للدفع عبر ماستر كارد.</p>
      <a href="https://mastercard.com/pay-link" target="_blank">
        <button>ادفع الآن</button>
      </a>
      <div class="actions">
        <button type="button" @click="emit('back')">السابق</button>
        <button type="button" @click="emit('next')">التالي</button>
      </div>
    </div>
  </template>
  <script setup>
  const emit = defineEmits(['next', 'back'])
  </script>
  