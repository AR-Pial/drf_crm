// src/mixins/formMixin.js
import axios from 'axios';

export default {
  data() {
    return {
      formData: {},
      error: null,
      success: null,
    };
  },
  methods: {
    async submitForm(endpoint) {
      try {
        await axios.post(endpoint, this.formData);
        this.success = 'Form submitted successfully!';
        this.resetForm();
      } catch (error) {
        this.error = error.response?.data?.detail || 'An error occurred';
      }
    },
    resetForm() {
      this.formData = {};
      this.error = null;
      this.success = null;
    },
  },
};
