<template>
	<div>
		<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog modal-lg">
			<div class="modal-content">
				<div class="modal-header">
				<h5 class="modal-title" id="exampleModalLabel">{{ modalHeaderName }}</h5>
				<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				</div>
				<div class="modal-body">
					<slot name="body"></slot>
				</div>		
			</div>
			</div>
		</div>
	</div>
</template>
  
<script>
  export default {
	props: {
		modalHeaderName: String, // Define the prop for the button name
  },
  };
</script>
  