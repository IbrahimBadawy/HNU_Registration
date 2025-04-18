
<!-- 📁 frontend/src/steps/GuardianInfo.vue -->
<template>
    <div class="step">
      <h2>بيانات ولي الأمر</h2>
      <form @submit.prevent="handleNext">
        <input v-model="form.guardian_name" placeholder="اسم ولي الأمر" required />
        <input v-model="form.guardian_relation" placeholder="صلة القرابة" required />
        <input v-model="form.guardian_phone" placeholder="رقم الهاتف" required />
        <input v-model="form.guardian_email" placeholder="البريد الإلكتروني" />
        <input v-model="form.guardian_job" placeholder="الوظيفة" required />
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
    guardian_name: store.formData.guardian_name,
    guardian_relation: store.formData.guardian_relation,
    guardian_phone: store.formData.guardian_phone,
    guardian_email: store.formData.guardian_email,
    guardian_job: store.formData.guardian_job
  })
  const handleNext = () => {
    store.updateForm(form)
    emit('next')
  }
  </script>