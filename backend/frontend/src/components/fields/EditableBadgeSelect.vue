<template>
	<div>
		<div class=" text-muted text-dark text-start">
			<div v-if="!editing" class="d-flex">
				<p>{{ label }}: <span class="badge bg-secondary px-2 py-1" >{{ valueName }}</span></p>  
				<a class="ms-2" href="#" @click="toggleEdit">edit</a>
			</div>
			<div v-else class="d-flex my-1">
				<label class="" for="">{{ label }}: </label>
				<div class="">
					<select class="form-select form-select-sm" v-model="editedValue">
						<option v-for="option in options" :value="option.id" >{{ option.first_name }} {{ option.last_name }} {{ option.label }}</option>
					</select>
				</div>

				<span class="d-flex">
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
		props:{
			label: String,
			value: String,
			valueName: String,
			opportunityFieldname: String,
    		editUrl: String,
			optionUrl: String,
			fieldName: String,			
		},
		data(){
			return{
				editing: false,
				editedValue: this.value,
				editedValueName: this.valueName,
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
			async saveValue() {
	
				try {
					await this.editField(this.editUrl, this.opportunityFieldname, this.editedValue);
					this.editing = false;
				} catch (error) {
					console.error(error);
				}
			},
			cancelEdit(){
				this.editing = false;
				this.editedValue = this.value;
				this.editedValueName = this.valueName;
			},
			editSuccess(obj=null){
				// location.reload();
				console.log(obj)
				if(obj){
					this.editedValueName = obj[this.fieldName];
				}

				this.$emit('update:value', this.editedValue,this.fieldName, this.editedValueName);
			},
			async fetchOptions(){

				if (this.fieldName === 'stage') {
					this.options = [
						{ id: 'Unassigned', label: 'Unassigned' },
						{ id: 'Assigned', label: 'Assigned' },
						{ id: 'Lead', label: 'Lead' },
						{ id: 'Unsuccessful', label: 'Unsuccessful' },
						{ id: 'Successful', label: 'Successful' },
					];
        		}
				else{
					try {
					const response = await this.$axios.get(this.optionUrl);
					this.options = response.data; 
					console.log(this.options);
					} catch (error) {
						console.error(error);
					}

				}

			}
		},
		mounted() {
			this.fetchOptions()
		},
	};

</script>