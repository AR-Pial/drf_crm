<template>

<div>
	<div class="text-muted text-dark text-start "> 
		
		<div v-if="!editing" class="d-flex">
			<p>{{ label }}: <span class="badge bg-secondary px-2 py-1" >{{ value }}</span></p>  
			<a class="ms-2" href="#" @click="toggleEdit">edit</a>
		</div>
		
		<div v-else class="editable my-1">
			<input class="" type="text"  v-model="editedValue" />
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
import EditFieldMixin from '@/mixins/editFieldMixin.js';
	export default{
		mixins: [EditFieldMixin],
		props: {
			label: String,
			value: String,
			opportunityFieldname: String,
    		editUrl: String,
		},

		data (){
			return {
				editing: false,
				editedValue: this.value,
			};
		},
		methods: {
			toggleEdit() {
				if (this.editing) {
					this.cancelEdit();
				} else {
					this.editing = true;
				}
			},

			async saveValue() {
				if (this.editedValue.trim() === '') {
					return; 
				}
				console.log(this.editedValue);

				try {
					console.log(this.editedValue);
				 	await this.editField(this.editUrl, this.opportunityFieldname, this.editedValue);
					this.editing = false;
				} catch (error) {
					console.error(error);
				}
			},

			cancelEdit() {
				this.editing = false;
				this.editedValue = this.value;
			},
		}
	};
</script>