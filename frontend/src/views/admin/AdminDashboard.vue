
... المحتويات السابقة ...

<!-- 📁 frontend/src/views/admin/AdminDashboard.vue -->
<template>
  <div class="dashboard">
    <h2>لوحة تحكم الأدمن</h2>
    <div class="stats" v-if="report">
      <p><strong>إجمالي الطلبات:</strong> {{ report.total }}</p>
      <p><strong>مقبول:</strong> {{ report.accepted }}</p>
      <p><strong>مرفوض:</strong> {{ report.rejected }}</p>
      <p><strong>قيد المراجعة:</strong> {{ report.pending }}</p>
    </div>
    <div class="filters">
      <input v-model="filters.college" placeholder="فلترة حسب الكلية" />
      <select v-model="filters.status">
        <option value="">كل الحالات</option>
        <option value="pending">قيد المراجعة</option>
        <option value="accepted">مقبول</option>
        <option value="rejected">مرفوض</option>
      </select>
      <button @click="fetchApplications">تحديث</button>
      <button @click="exportToExcel">تصدير إلى Excel</button>
    </div>

    <table v-if="applications.length">
      <thead>
        <tr>
          <th>الاسم</th>
          <th>الرقم القومي</th>
          <th>الكلية</th>
          <th>الحالة</th>
          <th>تفاصيل</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="app in applications" :key="app.id">
          <td>{{ app.full_name_ar }}</td>
          <td>{{ app.national_id }}</td>
          <td>{{ app.desired_college }}</td>
          <td>{{ statusMap[app.status] }}</td>
          <td>
            <router-link :to="`/admin/application/${app.id}`">عرض</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const applications = ref([])
const filters = ref({ college: '', status: '' })
const router = useRouter()
const report = ref(null)

const statusMap = {
  pending: 'قيد المراجعة',
  accepted: 'مقبول',
  rejected: 'مرفوض'
}

const fetchApplications = async () => {
  const params = {}
  if (filters.value.college) params.college = filters.value.college
  if (filters.value.status) params.status = filters.value.status

  const res = await axios.get('/api/admin/applications/', {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`
    },
    params
  })
  applications.value = res.data
}

const fetchReport = async () => {
  const res = await axios.get('/api/admin/report/', {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`
    }
  })
  report.value = res.data
}


const exportToExcel = async () => {
  const res = await axios.get('/api/export/excel/', {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('access')}`
    },
    responseType: 'blob'
  })
  const url = window.URL.createObjectURL(new Blob([res.data]))
  const link = document.createElement('a')
  link.href = url
  link.setAttribute('download', 'applications.xlsx')
  document.body.appendChild(link)
  link.click()
}

onMounted(async () => {
  try {
    await axios.get('/api/check/admin/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }
    })
  } catch {
    router.push('/admin/login')
  }
})

fetchApplications()
fetchReport()
</script>


<style scoped>
.dashboard {
  max-width: 1000px;
  margin: auto;
  padding: 20px;
}
.stats {
  display: flex;
  gap: 20px;
  margin-bottom: 15px;
  font-size: 1rem;
  color: #333;
}
.filters {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
input, select, button {
  padding: 10px;
  font-size: 1rem;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ccc;
  padding: 8px;
  text-align: center;
}
th {
  background-color: #f2f2f2;
}
</style>