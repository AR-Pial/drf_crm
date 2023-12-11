<template>
	<div>
		<div class="card mx-2 mx-lg-5 my-5 shadow">
			<h5 class="card-header bg-secondary text-white text-start d-flex align-items-center">       
				{{fieldTitle }}
				<a class="text-white ms-auto" href="">Edit</a>
			</h5>
			<div class="card-body">
				<p class="text-muted text-dark text-start " style="white-space: pre-wrap;"> {{ fieldValue }}</p>        
			</div>
		</div>
	</div>
</template>

<script>

export default {
	props: {
		fieldTitle: String,
		fieldValue: String
	}
}

</script>