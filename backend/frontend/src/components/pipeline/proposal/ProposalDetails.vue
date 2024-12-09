<template>
  <div>
    <div class="px-3 py-2" v-if="proposal">
      <h4 class="py-2 text-success">{{  proposal.title  }}</h4>
      <div class="d-flex flex-column mx-2 mx-lg-4 gap-4">
          <EditableBadgeField label="Proposal Title" :value="proposal.title" @update:value="updateProposalField"
          Fieldname="title" :editUrl="editUrl"    
          /> 
          <EditableCardField fieldTitle="Remarks" :fieldValue="proposal.remarks" @update:fieldValue="updateProposalField"
          Fieldname="remarks"   :editUrl="editUrl"/>
          <EditableCardField fieldTitle="Details" :fieldValue="proposal.details" @update:fieldValue="updateProposalField"
          Fieldname="details"   :editUrl="editUrl"/>
      </div>
          
    </div>
  </div>
</template>

<script>
import { endpoints } from '@/api';
import EditableBadgeField from '../../fields/EditableBadgeField.vue';
import EditableCardField from '../../fields/EditableCardField.vue';

export default {
  components: {
    EditableBadgeField,
    EditableCardField
  },
  data(){
    return{
      proposal: null,
      proposalUuid: this.$route.params.uuid
    }
  },
  computed: {
    // Construct the edit URL dynamically using `endpoints`
    editUrl() {
      return `${endpoints.proposal}/${this.proposalUuid}/`;
    }
  },
  methods: {
    fetchProposal() {
      
      const url = `${endpoints.proposal}/${this.proposalUuid}/`;
      console.log("fetch proposal"+ url)
      this.$axios.get(url)
        .then(response => {
          this.proposal = response.data;
          console.log(this.proposal)
        })
        .catch(error => {
          console.error('Error fetching proposals:', error);
        });
    },
    // New method to handle updates from EditableBadgeField
    updateProposalField(newValue, fieldName) {
    console.log('Updating field:', fieldName);
    console.log('New value:', newValue);

    // Update the local proposal object directly
    if (this.proposal) {
      this.proposal[fieldName] = newValue;
    }
  }

  },
  mounted(){
    this.fetchProposal()
  }
}
</script>

<style>

</style>