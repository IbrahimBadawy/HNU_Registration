
<template>
    <div class="track-container">
      <h2>تتبع حالة الطلب</h2>
      <button @click="fetchStatus">تحديث الحالة</button>
      <div v-if="status">
        <p><strong>الحالة:</strong> {{ statusMap[status] }}</p>
        <p v-if="rejectionReason"><strong>سبب الرفض:</strong> {{ rejectionReason }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'

  const status = ref('')
  const rejectionReason = ref('')
  const router = useRouter()

  const statusMap = {
    pending: 'قيد المراجعة',
    accepted: 'مقبول',
    rejected: 'مرفوض'
  }
  
  onMounted(async () => {
  try {
    await axios.get('/api/check/student/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }
    })
    fetchStatus()
  } catch {
    router.push('/login')
  }
})
const fetchStatus = async () => {
  const res = await axios.get('/api/application/', {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`
    }
  })
  status.value = res.data.status
  rejectionReason.value = res.data.rejection_reason
}
  </script>
  
  <style scoped>
  .track-container {
    max-width: 500px;
    margin: auto;
    text-align: center;
  }
  button {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 1rem;
    background-color: #1976d2;
    color: white;
    border: none;
    cursor: pointer;
  }
  p {
    font-size: 1.1rem;
    margin-top: 10px;
  }
  </style>