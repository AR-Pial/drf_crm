export default {
  methods: {
    async editField(editUrl,fieldname, newValue) {
      try {
        const response = await this.$axios.patch(editUrl, {
          [fieldname]: newValue,
        });

        if (response.status === 200) {
          // Success!
          this.editSuccess(response.data);
        } else {
          // Something went wrong
          console.error(response);
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};


// #old
// export default {
//   methods: {
//     async editField(editUrl, fieldname, newValue) {
// 		console.log(fieldname)
// 		console.log(newValue)
// 		console.log(editUrl)
// 		const requestData = {
// 			field_name: fieldname, // Pass the field name
// 			new_value: newValue,   // Pass the new value
// 		};
// 		const data = {
// 			[fieldname]: newValue,
// 		};
// 		this.$axios
// 		.post(editUrl, requestData)
// 		.then(response => {
// 		  // Handle the response if needed
// 		  console.log('Field updated successfully:', response);
// 		  this.$emit('update:value', newValue,fieldname);
// 		})
// 		.catch(error => {
// 		  // Handle errors
// 		  console.error('Error updating field:', error);
// 		});
//     },
//   },
// };
