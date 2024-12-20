<template>
    <div>
      <!-- Use the CreateModalHelper component -->
      <edit-modal-helper ref="editProposalModal" editModalHeaderName="Edit Proposal" @submitForm="updateProposal">
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
  import { endpoints } from '@/api';
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
    methods: {
      async updateProposal() {
        console.log("submit edit" + this.editProposal.uuid);
        try {
          const formData = new FormData();
          formData.append('title', this.editProposal.title);
          formData.append('details', this.editProposal.details);
          formData.append('remarks', this.editProposal.remarks);
          if (this.editProposal.file) {
            formData.append('file', this.editProposal.file);
          }

          const url = `${endpoints.proposal}/${this.editProposal.uuid}/`;
          const response = await this.$axios.put(url, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
          });
          console.log("Response : ", response)
          this.$emit('proposalUpdated');
          this.resetForm();
          this.$refs.editProposalModal.closeModal();
          
        } catch (error) {
          console.error('Error updating proposal:', error);
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
    }

  };
  </script>

  <style scoped>
  /* Add any custom styles for CreateProposal */
  </style>

  
   
  