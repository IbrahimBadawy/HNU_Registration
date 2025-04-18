

// 📁 frontend/src/views/ApplicationWizard.vue

<template>
  <div>
    <component :is="currentComponent" @next="next" @back="back" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useApplicationStore } from '@/stores/application'
import { onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

import PersonalInfo from '@/steps/PersonalInfo.vue'
import AcademicInfo from '@/steps/AcademicInfo.vue'
import GuardianInfo from '@/steps/GuardianInfo.vue'
import HealthInfo from '@/steps/HealthInfo.vue'
import DocumentUpload from '@/steps/DocumentUpload.vue'
import Payment from '@/steps/Payment.vue'
import Submit from '@/steps/Submit.vue'

const steps = [
  PersonalInfo,
  AcademicInfo,
  GuardianInfo,
  HealthInfo,
  DocumentUpload,
  Payment,
  Submit
]
const router = useRouter()

const store = useApplicationStore()
const currentComponent = computed(() => steps[store.currentStep - 1])

const next = () => store.nextStep()
const back = () => store.prevStep()
onMounted(async () => {
  try {
    await axios.get('/api/check/student/', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }
    })
  } catch {
    router.push('/login')
  }
})
</script>