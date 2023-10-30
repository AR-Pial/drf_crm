<template>
	<div>
		<div class=" text-muted text-dark text-start">
			<div v-if="!editing" class="d-flex">
				<p>{{ label }}: <span class="badge bg-secondary px-2 py-1" >{{ valueName }}</span></p>  
				<a class="ms-2" href="#" @click="toggleEdit">edit</a>
			</div>
			<div v-else class=" my-1">
				<select v-model="editedValue">
					<option v-for="option in options" :value="option.id">{{ option.first_name }} {{ option.last_name }}</option>
				</select>
				<span>
				<a class="ms-2" href="#" @click="saveValue">
					<i class="fas fa-check"></i> <!-- Check icon for saving -->
				</a>
				<a class="ms-2" href="#" @click="cancelEdit">
					<i class="fas fa-times"></i> <!-- Cancel icon for canceling -->
				</a>
				</span>
			</div>
		</div>
	</div>
</template>

<script>
	export default{

		props:{
			label: String,
			value: String,
			valueName: String, 
			optionUrl: String,
		},
		data(){
			return{
				editing: false,
				editedValue: this.value,
				options: [],
			}
		},
		methods:{
			toggleEdit() {
				if (this.editing) {
					this.cancelEdit();
				} else {
					this.editing = true;
				}
			},
			cancelEdit(){
				this.editing = false;
			},
			async fetchOptions(){
				try {
					const response = await this.$axios.get(this.optionUrl);
					this.options = response.data; 
				} catch (error) {
					console.error(error);
      			}
			}
		},
		mounted() {
			this.fetchOptions()
		},
	};

</script>