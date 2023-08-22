<template>
  <div>
    <form @submit.prevent="handleFormSubmit">
		<slot name="body"></slot>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  methods: {
    handleFormSubmit() {
      // If the parent component has the submitForm method, call it
      if (this.$parent.submitForm) {
        this.$parent.submitForm();
      } else {
        // Otherwise, emit an event to notify the parent component
        this.$emit('submitForm');
      }
    }
  }
};
</script>