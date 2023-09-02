<template>
  <div>
    <form @submit.prevent="handleFormSubmit" enctype="multipart/form-data">
		<slot name="body"></slot>
    <div class="text-end me-1 me-lg-2">
      <slot name="close"></slot>
      <button class="btn btn-primary" type="submit">Submit</button>
    </div>
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