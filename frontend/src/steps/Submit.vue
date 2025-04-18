

  <!-- 📁 frontend/src/steps/Submit.vue -->
  <template>
    <div class="step">
      <h2>مراجعة وإرسال الطلب</h2>
      <p>تم إدخال جميع البيانات. اضغط على زر الإرسال لإنهاء العملية.</p>
      <div class="actions">
        <button type="button" @click="emit('back')">السابق</button>
        <button @click="submit">إرسال</button>
      </div>
    </div>
  </template>
  <script setup>
  import { useApplicationStore } from '@/stores/application'
  const store = useApplicationStore()
  const emit = defineEmits(['back'])
  const submit = async () => {
    await store.submitToServer()
    alert('تم إرسال الطلب بنجاح')
    window.location.href = '/track'
  }
  </script>