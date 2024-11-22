<template>
    <div>
      <form @submit.prevent="submitForm">
        <div v-for="(field, index) in fields" :key="index">
          <DynamicField 
            :name="field.name"
            :label="field.label"
            :type="field.type"
            :value="formData[field.name]"
            :options="field.options || []"
            v-model="formData[field.name]"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import DynamicField from './DynamicField.vue';
  
  export default {
    components: {
      DynamicField
    },
    data() {
      return {
        fields: [],  // Fields retrieved from the API
        formData: {} // Stores the form input values
      };
    },
    methods: {
      // Fetch the fields from the API
      async fetchFields() {
        const response = await axios.get('/api/get-fields/');
        this.fields = response.data.fields;
        // Initialize formData keys based on field names
        this.fields.forEach(field => {
          this.formData[field.name] = '';
        });
      },
      // Handle form submission
      async submitForm() {
        const response = await axios.post('/api/submit-form/', this.formData);
        // Handle response
      }
    },
    mounted() {
      this.fetchFields(); // Fetch fields when the component is mounted
    }
  };
  </script>
  