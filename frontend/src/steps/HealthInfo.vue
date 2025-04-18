

<!-- 📁 frontend/src/steps/HealthInfo.vue -->
<template>
    <div class="step">
      <h2>البيانات الصحية</h2>
      <form @submit.prevent="handleNext">
        <textarea v-model="form.illnesses" placeholder="أمراض مزمنة"></textarea>
        <textarea v-model="form.disabilities" placeholder="إعاقات أو احتياجات خاصة"></textarea>
        <textarea v-model="form.allergies" placeholder="حساسية من أدوية أو أطعمة"></textarea>
        <input v-model="form.emergency_contact" placeholder="رقم للتواصل في الطوارئ" required />
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
    illnesses: store.formData.illnesses,
    disabilities: store.formData.disabilities,
    allergies: store.formData.allergies,
    emergency_contact: store.formData.emergency_contact
  })
  const handleNext = () => {
    store.updateForm(form)
    emit('next')
  }
  </script>