
export default {
  methods: {
    async editField(editUrl, fieldname, newValue) {
		console.log(fieldname)
		console.log(newValue)
		console.log(editUrl)
		const requestData = {
			field_name: fieldname, // Pass the field name
			new_value: newValue,   // Pass the new value
		};
		const data = {
			[fieldname]: newValue,
		};
		this.$axios
		.post(editUrl, requestData)
		.then(response => {
		  // Handle the response if needed
		  console.log('Field updated successfully:', response);
		  this.$emit('update:value', newValue,fieldname);
		})
		.catch(error => {
		  // Handle errors
		  console.error('Error updating field:', error);
		});
    },
  },
};

// #old
// import axios from 'axios';

// export default {
//   methods: {
//     async editField(editUrl, uuid, fieldname, newValue) {
//       try {
//         const response = await axios.put(editUrl, {
//           [fieldname]: newValue,
//         });

//         if (response.status === 200) {
//           // Success!
//           this.$emit('update:value', newValue,fieldname);
//         } else {
//           // Something went wrong
//           console.error(response);
//         }
//       } catch (error) {
//         console.error(error);
//       }
//     },
//   },
// };