// 📁 frontend/src/stores/application.js

import { defineStore } from "pinia";
import axios from "axios";

export const useApplicationStore = defineStore("application", {
  state: () => ({
    formData: {
      full_name_ar: "",
      full_name_en: "",
      national_id: "",
      gender: "",
      birth_date: "",
      nationality: "",
      phone: "",
      address: "",
      city: "",
      governorate: "",
      certificate_type: "",
      grad_year: "",
      total_score: "",
      percentage: "",
      desired_college: "",
      guardian_name: "",
      guardian_relation: "",
      guardian_phone: "",
      guardian_email: "",
      guardian_job: "",
      illnesses: "",
      disabilities: "",
      allergies: "",
      emergency_contact: "",
    },
    currentStep: 1,
  }),

  actions: {
    updateForm(data) {
      this.formData = { ...this.formData, ...data };
    },
    nextStep() {
      if (this.currentStep < 7) this.currentStep++;
    },
    prevStep() {
      if (this.currentStep > 1) this.currentStep--;
    },
    async submitToServer() {
      await axios.post("/api/application/", this.formData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access")}`,
        },
      });
    },
  },
});
