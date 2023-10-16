<template>
	<div class="bg-white p-2 p-lg-3 rounded">
		<div class="d-flex mb-1 mb-lg-2">
			<h5><slot name="table-name"></slot></h5>
			<button type="button" class="btn btn-primary ms-auto" data-bs-toggle="modal" data-bs-target="#exampleModal">
				<svg xmlns="http://www.w3.org/2000/svg"  height="1.15em" viewBox="0 0 448 512" style="fill: white;">
					<path d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"/>
				</svg> <span class="ps-1">{{ addButtonName }}</span>  
			</button>
		</div>
		
		<table class="table table-striped table-hover">
			
		<thead>
			<tr>
			<slot name="header"></slot>
			</tr>
		</thead>
		<tbody>
			<slot name="body"></slot>
		</tbody>
		</table>
	</div>
</template>
  
<script>
  export default {
	props: {
    addButtonName: String, // Define the prop for the button name
  },
  };
</script>
  