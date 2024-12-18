<template>
    <div>
      <!-- Use the CreateModalHelper component -->
      <edit-modal-helper ref="editProposalModal" editModalHeaderName="Edit Proposal" @submitForm="submitProposal">
        <template v-slot:body>
          <form>
            <!-- Use InputFields for each field in the form -->
            <div class="row justify-content-center p-2">
              <div class="col-12 col-lg-11">
                <input-fields
                  name="title"
                  label="Title"
                  type="text"
                  v-model="editProposal.title"
                ></input-fields>
              </div>
              
              <div class="col-12 col-lg-11">
                <input-fields
                  name="details"
                  label="Details"
                  type="textarea"
                  v-model="editProposal.details"
                ></input-fields>
              </div>
              <div class="col-12 col-lg-11">
                <input-fields
                  name="remarks"
                  label="Remarks"
                  type="textarea"
                  v-model="editProposal.remarks"
                ></input-fields>
              </div>
            </div>
          </form>
        </template>
      </edit-modal-helper>
    </div>
  </template>
  
  <script>
  import EditModalHelper from '@/components/helpers/EditModalHelper.vue';
  import InputFields from '@/components/fields/InputField.vue'; // Import InputFields
  
  export default {
    components: {
      "edit-modal-helper": EditModalHelper,
      "input-fields": InputFields, // Register InputFields component
    },
    data() {
      return {
        editProposal: {
          title: '',
          details: '',
          remarks: '',
          file: null 
        },
        // Options for the select field example
        categoryOptions: [
          { value: 'software', text: 'Software' },
          { value: 'hardware', text: 'Hardware' },
          { value: 'services', text: 'Services' }
        ]
      };
    },

  };
  </script>

  <style scoped>
  /* Add any custom styles for CreateProposal */
  </style>

  <!-- methods: {
     
     async submitProposal() {
       try {
         const opportunityUuid = this.$route.params.uuid;
         const formData = new FormData();
         formData.append('title', this.editProposal.title);
         formData.append('details', this.editProposal.details);
         formData.append('remarks', this.editProposal.remarks);
         formData.append('opportunity', opportunityUuid);
         
         // Append the file if it exists
         if (this.editProposal.file) {
           formData.append('file', this.editProposal.file);
         }
         console.log(this.editProposal)
         for (let pair of formData.entries()) {
           console.log(pair[0]+ ': ' + pair[1]);
         }
 
 
         // Send the FormData object in the POST request
         const response = await this.$axios.post('/deal/proposal/', formData, {
           headers: {
             'Content-Type': 'multipart/form-data'
           }
         });
 
         console.log('Proposal created:', response.data);
         this.resetForm(); // Reset the form fields
         this.$refs.editProposalModal.closeModal(); // Close the modal
       } catch (error) {
         console.error('Error creating proposal:', error);
       }
     },
     resetForm() {
       // Reset the form fields to their initial state
       this.editProposal = {
         title: '',
         details: '',
         remarks: '',
         file: null // Reset file as well
       };
     }
   } -->
  