
// 📁 frontend/src/steps/PersonalInfo.vue

<template>
  <div class="step">
    <h2>البيانات الشخصية</h2>
    <form @submit.prevent="handleNext">
      <input v-model="form.full_name_ar" placeholder="الاسم الكامل بالعربية" required />
      <input v-model="form.full_name_en" placeholder="الاسم الكامل بالإنجليزية" required />
      <input v-model="form.national_id" placeholder="الرقم القومي" required />
      <select v-model="form.gender" required>
        <option value="">-- النوع --</option>
        <option value="ذكر">ذكر</option>
        <option value="أنثى">أنثى</option>
      </select>
      <input type="date" v-model="form.birth_date" required />
      <input v-model="form.nationality" placeholder="الجنسية" required />
      <input v-model="form.phone" placeholder="رقم الهاتف" required />
      <input v-model="form.address" placeholder="العنوان" required />
      <input v-model="form.city" placeholder="المدينة" required />
      <input v-model="form.governorate" placeholder="المحافظة" required />

      <button type="submit">التالي</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { useApplicationStore } from '@/stores/application'

const store = useApplicationStore()
const emit = defineEmits(['next'])

const form = reactive({
  full_name_ar: store.formData.full_name_ar,
  full_name_en: store.formData.full_name_en,
  national_id: store.formData.national_id,
  gender: store.formData.gender,
  birth_date: store.formData.birth_date,
  nationality: store.formData.nationality,
  phone: store.formData.phone,
  address: store.formData.address,
  city: store.formData.city,
  governorate: store.formData.governorate
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
input, select, button {
  padding: 10px;
  font-size: 1rem;
}
button {
  background-color: #1976d2;
  color: white;
  border: none;
  cursor: pointer;
}
</style>