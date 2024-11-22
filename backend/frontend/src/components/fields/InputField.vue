<template>
    <div class="mb-3 text-start">
      <label :for="name" class="form-label">{{ label }}</label>
  
      <!-- Input Field (text, email, password, etc.) -->
      <input
        v-if="['text', 'password', 'email'].includes(type)"
        :type="type"
        :name="name"
        v-model="inputValue"
        class="form-control"
        @input="$emit('input', inputValue)"
      />
  
      <!-- Textarea Field -->
      <textarea
        v-if="type === 'textarea'"
        :name="name"
        v-model="inputValue"
        class="form-control"
        @input="$emit('input', inputValue)"
        rows="4"
      ></textarea>
  
      <!-- Select Field -->
      <select
        v-if="type === 'select'"
        :name="name"
        v-model="inputValue"
        class="form-select"
        @input="$emit('input', inputValue)"
      >
        <option v-for="option in options" :key="option.value" :value="option.value">
          {{ option.text }}
        </option>
      </select>
  
      <!-- Checkbox Field -->
      <div v-if="type === 'checkbox'" class="form-check">
        <input
          type="checkbox"
          :name="name"
          v-model="inputValue"
          class="form-check-input"
          @change="$emit('input', inputValue)"
        />
        <label class="form-check-label">{{ label }}</label>
      </div>
      
      <!-- Add more input types as needed -->
    </div>
  </template>
  
  <script>
  export default {
    props: {
      name: String,        // Field name
      label: String,       // Label for the field
      type: String,        // Input type (text, email, password, textarea, select, etc.)
      value: [String, Boolean, Number], // Value bound to the field
      options: Array       // Options for select fields (if any)
    },
    data() {
      return {
        inputValue: this.value || ""  // Local data for two-way binding
      };
    },
    watch: {
      value(newVal) {
        this.inputValue = newVal;
      }
    }
  };
  </script>
  