<template>
    <div>
      <!-- Bootstrap modal structure -->
      <div ref="modalRef" class="modal fade" id="createModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">{{ modalHeaderName }}</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <!-- Slot for the content of the modal body -->
              <slot name="body"></slot>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button @click="handleSubmit" type="button" class="btn btn-primary">Submit</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      modalHeaderName: {
        type: String,
        required: true
      },
    },
    mounted() {
      // Initialize Bootstrap modal
      this.modal = new bootstrap.Modal(this.$refs.modalRef);
    },
    methods: {
      openModal() {
        // Use Bootstrap's modal method to show the modal
        this.modal.show();
      },
      closeModal() {
        // Use Bootstrap's modal method to hide the modal
        this.modal.hide();
      },
      handleSubmit() {
        // Emit the submit event or call the parent component's submitForm method
        this.$emit('submitForm');
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any custom styles for the modal if necessary */
  </style>
  