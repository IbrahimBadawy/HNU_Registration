<template>
  <div class="detail">
    <h2>تفاصيل الطلب</h2>
    <div v-if="application">
      <p><strong>الاسم:</strong> {{ application.full_name_ar }}</p>
      <p><strong>الكلية المطلوبة:</strong> {{ application.desired_college }}</p>
      <p><strong>الحالة الحالية:</strong> {{ statusMap[application.status] }}</p>

      <textarea v-model="rejectionReason" placeholder="سبب الرفض (إن وُجد)" v-if="selectedStatus === 'rejected'"></textarea>

      <div class="actions">
        <select v-model="selectedStatus">
          <option disabled value="">اختر الحالة</option>
          <option value="accepted">قبول</option>
          <option value="rejected">رفض</option>
        </select>
        <button @click="submitReview">حفظ</button>
        <button @click="downloadPDF">تحميل PDF</button>
      </div>
    </div>
    <div v-else>جارٍ التحميل...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const application = ref(null)
const selectedStatus = ref('')
const rejectionReason = ref('')

const statusMap = {
  pending: 'قيد المراجعة',
  accepted: 'مقبول',
  rejected: 'مرفوض'
}

onMounted(async () => {
  try {
    await axios.get('/api/check/admin/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }
    })
    const res = await axios.get(`/api/admin/application/${route.params.id}/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }
    })
    application.value = res.data
  } catch {
    router.push('/admin/login')
  }
})

const submitReview = async () => {
  await axios.post('/api/admin/review/', {
    application: route.params.id,
    status: selectedStatus.value,
    rejection_reason: rejectionReason.value
  }, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`
    }
  })
  alert('تم حفظ التقييم')
  router.push('/admin')
}

const downloadPDF = async () => {
  const res = await axios.get(`/api/admin/pdf/${route.params.id}/`, {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`
    },
    responseType: 'blob'
  })
  const url = window.URL.createObjectURL(new Blob([res.data]))
  const link = document.createElement('a')
  link.href = url
  link.setAttribute('download', `application_${route.params.id}.pdf`)
  document.body.appendChild(link)
  link.click()
}
</script>