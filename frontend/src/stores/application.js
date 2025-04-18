// 📁 frontend/src/stores/application.js
import { defineStore } from "pinia";

export const useApplicationStore = defineStore("application", {
  state: () => ({
    form: {
      full_name_ar: "",
      national_id: "",
      phone: "",
      address: "",
      desired_college: "",
      guardian_name: "",
      health_notes: "",
      documents: [],
    },
  }),
  actions: {
    resetForm() {
      this.form = {
        full_name_ar: "",
        national_id: "",
        phone: "",
        address: "",
        desired_college: "",
        guardian_name: "",
        health_notes: "",
        documents: [],
      };
    },
  },
});
