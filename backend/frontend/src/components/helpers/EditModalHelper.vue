<template>
	<div>
		<div ref="editmodalRef" class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true" >
			<div class="modal-dialog modal-lg">
				<div class="modal-content">
					<div class="modal-header">
					<h5 class="modal-title" id="editModalLabel">{{ editModalHeaderName }}</h5>
					<button  type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					</div>
					<div class="modal-body">
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
		editModalHeaderName: String, // Define the prop for the button name
  },

  methods: {
    closeModal() {
		this.$refs.editmodalRef.classList.remove('show');
		this.$refs.editmodalRef.style.display = 'none';
		document.body.classList.remove('modal-open');
		const modalBackdrop = document.querySelector('.modal-backdrop');
		if (modalBackdrop) {
			modalBackdrop.remove();
		}
		
    },
	handleSubmit() {
		// If the parent component has the submitForm method, call it
		if(this.$parent.editSubmitForm){
			this.$parent.editSubmitForm();
		}
		else {
		// Otherwise, emit an event to notify the parent component
			this.$emit('submitForm');
		}
	}
  }

  };
</script>
  