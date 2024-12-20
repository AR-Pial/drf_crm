<template>
  <div>
    <div>
      <h5 class="py-2 py-lg-3 text-success">{{ opportunityName }}</h5>
    </div>
    <div class="col-12 col-lg-10 mx-auto my-3">
      <!-- Include the CreateProposal component -->
      <create-proposal ref="createProposalRef" @proposalCreated="refreshProposals"></create-proposal>
      <edit-proposal ref="editProposalRef" @proposalUpdated="refreshProposals"></edit-proposal>
      <table-helper :add-button-name="addButtonName">
        <template v-slot:table-name>
            Proposals
        </template>
        <template v-slot:header>
          <th>Title</th>
          <th>Remarks</th>
          <th>#</th>
          <th>Action</th>
        </template>

        <template v-slot:body>
            <tr v-for="proposal in proposals" :key="proposal.uuid">
              <td>{{ proposal.title }}</td>
              <td>{{ proposal.remarks }}</td>
              <td>
                <router-link :to="{ name: 'proposal-details', params: { uuid: proposal.uuid } }">
                  Details
                </router-link>
              </td>
              <td>
                <a href="" data-bs-toggle="modal" data-bs-target="#editModal" @click.prevent="openEditModal(proposal.uuid)" >Edit</a> / 
                <a href="">delete</a></td>
            </tr>
        </template>
      </table-helper>
    
    </div>
  </div>
</template>

<script>
import TableHelper from '@/components/helpers/TableHelper.vue';
import CreateProposal from './CreateProposal.vue';
import EditProposal from './EditProposal.vue';
import { endpoints } from '@/api';
export default {
    components: {
        "table-helper": TableHelper,
        "create-proposal": CreateProposal,
        "edit-proposal": EditProposal
    },
    data(){
      return{
        opportunityName: '',
        addButtonName: "Add Proposal",
        proposals: [],
        opportunityUuid: this.$route.params.uuid,
      }
    },
    methods: {
    fetchProposals() {
      const url = `${endpoints.proposal}/?opportunity_uuid=${this.opportunityUuid}`;
      this.$axios.get(url)
        .then(response => {
          this.proposals = response.data;
          console.log(this.proposals)
        })
        .catch(error => {
          console.error('Error fetching proposals:', error);
        });
    },
    refreshProposals() {
      this.fetchProposals(); // Refresh the list of proposals or take other actions
    },
    fetchOpportunityDetails() {
      const url = `${endpoints.opportunity}/${this.opportunityUuid}/`;
      this.$axios.get(url)
        .then(response => {
          this.opportunityName = response.data.name;  // Assuming the response has a 'name' field
          console.log(this.opportunityName )
        })
        .catch(error => {
          console.error('Error fetching opportunity details:', error);
        });
    },

    openEditModal(proposalUuid) {
      const url = `${endpoints.proposal}/${proposalUuid}/`;
      this.$axios.get(url)
        .then(response => {
          const proposalData = response.data;
          console.log(proposalData)
          this.$refs.editProposalRef.editProposal = {
            uuid: proposalData.uuid,
            title: proposalData.title,
            details: proposalData.details,
            remarks: proposalData.remarks,
            file: null,
          };
        })
        .catch(error => {
          console.error('Error fetching proposal:', error);
        });
    },
  },
  mounted() {
    this.fetchOpportunityDetails();
    this.fetchProposals();
  },
}
</script>

<style>

</style>