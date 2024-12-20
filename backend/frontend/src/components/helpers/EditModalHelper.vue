<template>
	<div>
	  <!-- Bootstrap modal structure for Edit Modal -->
	  <div ref="editmodalRef" class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
		<div class="modal-dialog modal-lg">
		  <div class="modal-content">
			<div class="modal-header">
			  <h5 class="modal-title" id="editModalLabel">{{ editModalHeaderName }}</h5>
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
	  editModalHeaderName: {
		type: String,
		required: true
	  },
	},
	mounted() {
	  // Initialize Bootstrap modal using the modal reference
	  this.modal = new bootstrap.Modal(this.$refs.editmodalRef);
	},
	methods: {
	  openModal() {
		// Open the modal using Bootstrap's method
		this.modal.show();
	  },
	  closeModal() {
		// Close the modal using Bootstrap's method
		this.modal.hide();
	  },
	  handleSubmit() {
		// Emit the submit event or call the parent component's oppEditSubmitForm method
		
		if(this.$parent.oppEditSubmitForm){
			this.$parent.oppEditSubmitForm();
		}
		else {
		// Otherwise, emit an event to notify the parent component
			this.$emit('submitForm');
		}
	  }
	}
  };
  </script>
  
  <style scoped>
  /* Custom styles for the modal if needed */
  </style>
  