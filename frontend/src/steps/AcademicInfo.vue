

<!-- 📁 frontend/src/steps/AcademicInfo.vue -->

<template>
    <div class="step">
      <h2>البيانات الأكاديمية</h2>
      <form @submit.prevent="handleNext">
        <input v-model="form.certificate_type" placeholder="نوع الشهادة" required />
        <input v-model="form.grad_year" type="number" placeholder="سنة التخرج" required />
        <input v-model="form.total_score" type="number" step="0.01" placeholder="المجموع الكلي" required />
        <input v-model="form.percentage" type="number" step="0.01" placeholder="النسبة المئوية" required />
        <input v-model="form.desired_college" placeholder="الكلية المطلوبة" required />
  
        <div class="actions">
          <button type="button" @click="emit('back')">السابق</button>
          <button type="submit">التالي</button>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
  import { reactive } from 'vue'
  import { useApplicationStore } from '@/stores/application'
  
  const store = useApplicationStore()
  const emit = defineEmits(['next', 'back'])
  
  const form = reactive({
    certificate_type: store.formData.certificate_type,
    grad_year: store.formData.grad_year,
    total_score: store.formData.total_score,
    percentage: store.formData.percentage,
    desired_college: store.formData.desired_college
  })
  
  const handleNext = () => {
    store.updateForm(form)
    emit('next')
  }
  </script>
  
  <style scoped>
  .step {
    max-width: 500px;
    margin: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .actions {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
  }
  button {
    padding: 10px;
    font-size: 1rem;
    background-color: #1976d2;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>