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
    />

    <!-- Textarea Field -->
    <textarea
      v-if="type === 'textarea'"
      :name="name"
      v-model="inputValue"
      class="form-control"
      rows="4"
    ></textarea>

    <!-- Select Field -->
    <select
      v-if="type === 'select'"
      :name="name"
      v-model="inputValue"
      class="form-select"
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
      />
      <label class="form-check-label">{{ label }}</label>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: String,        // Field name
    label: String,       // Label for the field
    type: String,        // Input type (text, email, password, textarea, select, etc.)
    modelValue: [String, Boolean, Number], // Use modelValue instead of value
    options: Array       // Options for select fields (if any)
  },
  computed: {
    inputValue: {
      get() {
        return this.modelValue;  // Getter for modelValue
      },
      set(newValue) {
        this.$emit('update:modelValue', newValue);  // Emit update event to parent
      }
    }
  }
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
