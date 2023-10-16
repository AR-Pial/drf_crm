// EditAllFieldsMixin.js
export const EditAllFieldsMixin = {
	data() {
	  return {
		editedData: {}, // Use an object to store data for all fields
		isEditing: false,
	  };
	},
	methods: {
	  startEditing(data) {
		this.isEditing = true;
		this.editedData = { ...data };
	  },
	  saveField(fieldName, value) {
		// Make an API call to update the specific field value
		const { url, id } = this.editedData;
		const dataToUpdate = { [fieldName]: value };
		
		axios.put(`${url}/${id}/`, dataToUpdate)
		  .then(response => {
			// Update the component's data with the updated field value
			this.$set(this.editedData, fieldName, response.data[fieldName]);
			this.isEditing = false;
		  })
		  .catch(error => {
			console.error(error);
		  });
	  },
	  cancelEdit() {
		this.isEditing = false;
	  },
	},
  };