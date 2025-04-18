
<!-- 📁 frontend/src/steps/DocumentUpload.vue -->
<template>
    <div class="step">
      <h2>رفع المستندات</h2>
      <input type="file" @change="handleFileUpload" multiple />
      <div class="actions">
        <button type="button" @click="emit('back')">السابق</button>
        <button type="button" @click="emit('next')">التالي</button>
      </div>
    </div>
  </template>
  <script setup>
  import axios from 'axios'
  const emit = defineEmits(['next', 'back'])
  const handleFileUpload = async (e) => {
    const files = e.target.files
    for (const file of files) {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('doc_type', file.name)
      await axios.post('/api/upload/', formData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access')}`,
          'Content-Type': 'multipart/form-data'
        }
      })
    }
  }
  </script>
  
