<template>
	<div>
		<div v-if="!editing">
			<div class="card mx-2 mx-lg-5 my-5 shadow">
				<h5 class="card-header bg-secondary text-white text-start d-flex align-items-center">       
					{{fieldTitle }}
					<a class="text-white ms-auto cursor-pointer" @click="toggleEdit">Edit</a>
				</h5>
				<div class="card-body">
					<p class="text-muted text-dark text-start " style="white-space: pre-wrap;"> {{ fieldValue }}</p>        
				</div>
			</div>
		</div>
		<div v-else class="card rounded editable mx-2 mx-lg-5 my-5 shadow">
			<div class="card-header text-end bg-secondary py-1">
				<a class="mx-1 mx-lg-2 cursor-pointer text-white" @click="saveValue">
					<i class="fas fa-check"></i>
				</a>
				<a class="mx-1 mx-lg-2 cursor-pointer text-white" @click="cancelEdit">
					<i class="fas fa-times"></i> 
				</a>
			</div>
			<textarea class="form-control card-body rounded-0" rows="10" type="text"  v-model="editedValue">
			</textarea>
			<div class="text-end bg-secondary rounded-bottom">
				<button class="btn btn-sm btn-danger m-1 m-lg-2" @click="cancelEdit">Close</button>
				<button class="btn btn-sm btn-primary m-1 m-lg-2" @click="saveValue">Submit</button>
			</div>
			
		</div>	
	</div>
</template>

<script>
import EditFieldMixin from '@/mixins/editFieldMixin.js';
export default {
	mixins: [EditFieldMixin],
	props: {
		fieldTitle: String,
		fieldValue: String,
		opportunityFieldname: String,
    	editUrl: String,
	},
	data(){
		return {
			editing: false,
			editedValue: this.fieldValue,
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
			if (this.editedValue.trim() === '') {
					return; 
				}
				console.log(this.editedValue);

			try {
				await this.editField(this.editUrl, this.opportunityFieldname, this.editedValue);
				this.editing = false;
			} catch (error) {
				console.error(error);
			}
		},
		editSuccess(){
				this.$emit('update:fieldValue', this.editedValue,this.opportunityFieldname);
		},
		cancelEdit() {
				this.editing = false;
				this.editedValue = this.fieldValue;
		},

	}
}

</script>