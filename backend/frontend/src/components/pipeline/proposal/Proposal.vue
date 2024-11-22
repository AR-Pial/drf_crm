<template>
  <div>
    <div class="col-12 col-lg-10 mx-auto my-3">
      <!-- Include the CreateProposal component -->
      <create-proposal ref="createProposalRef"></create-proposal>
      <table-helper :add-button-name="addButtonName">
        <template v-slot:table-name>
            Proposals
        </template>
        <template v-slot:header>
          <th>Name</th>
          <th>Company Name</th>
          <th>Stage</th>
          <th>Details</th>
          <th>Action</th>
        </template>

        <template v-slot:body>
            <tr>
              <td>ok</td>
              <td>ok</td>
              <td>ok</td>
              <td>ok</td>
              <td>ok</td>
            </tr>
        </template>
      </table-helper>
    
    </div>
  </div>
</template>

<script>
import TableHelper from '@/components/helpers/TableHelper.vue';
import CreateProposal from './CreateProposal.vue';
export default {
    components: {
        "table-helper": TableHelper,
        "create-proposal": CreateProposal,
    },
    data(){
      return{
        addButtonName: "Add Proposal",
      }
    }
}
</script>

<style>

</style>