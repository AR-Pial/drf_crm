<template>
  <div>
    <!-- Use the CreateModalHelper component -->
    <create-modal-helper ref="createProposalModal" :modalHeaderName="'Add New Proposal'" @submitForm="submitProposal">
      <template v-slot:body>
        <form>
          <!-- Use InputFields for each field in the form -->
          <div class="row justify-content-center p-2">
            <div class="col-12 col-lg-11">
              <input-fields
                name="title"
                label="Title"
                type="text"
                v-model="newProposal.title"
              ></input-fields>
            </div>
            
            <div class="col-12 col-lg-11">
              <input-fields
                name="details"
                label="Details"
                type="textarea"
                v-model="newProposal.details"
              ></input-fields>
            </div>
            <div class="col-12 col-lg-11">
              <input-fields
                name="remarks"
                label="Remarks"
                type="textarea"
                v-model="newProposal.remarks"
              ></input-fields>
            </div>
          </div>
        </form>
      </template>
    </create-modal-helper>
  </div>
</template>

<script>
import CreateModalHelper from '@/components/helpers/CreateModalHelper.vue';
import InputFields from '@/components/fields/InputField.vue'; // Import InputFields

export default {
  components: {
    "create-modal-helper": CreateModalHelper,
    "input-fields": InputFields, // Register InputFields component
  },
  data() {
    return {
      newProposal: {
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
    openModal() {
      // Open the modal using the reference to CreateModalHelper
      this.$refs.createProposalModal.openModal();
    },
    async submitProposal() {
      try {
        const opportunityUuid = this.$route.params.uuid;
        const formData = new FormData();
        formData.append('title', this.newProposal.title);
        formData.append('details', this.newProposal.details);
        formData.append('remarks', this.newProposal.remarks);
        formData.append('opportunity', opportunityUuid);
        
        // Append the file if it exists
        if (this.newProposal.file) {
          formData.append('file', this.newProposal.file);
        }
        console.log(this.newProposal)
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
        this.$refs.createProposalModal.closeModal(); // Close the modal
      } catch (error) {
        console.error('Error creating proposal:', error);
      }
    },
    resetForm() {
      // Reset the form fields to their initial state
      this.newProposal = {
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
