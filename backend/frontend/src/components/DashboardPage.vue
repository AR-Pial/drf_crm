<template>
  <div>
      <h4 class="py-2">Welcome, {{ $user_full_name }}</h4>

      <div v-if="$user_type == 'agent'">
        <div class="container py-2">
          <table-helper>
            <template v-slot:table-name>
                Your Opportunities
            </template>
            <template v-slot:header>
              <th>Name</th>
              <th>Company Name</th>
              <th>Manager</th>
              <th>Stage</th>
              <th>Details</th>
            </template>

            <template v-slot:body>
              <tr v-for="opportunity in opportunities" :key="opportunity.id">
                <td>{{ opportunity.name }}</td>
                <td>{{ opportunity.company_name }}</td>
                <td>{{ opportunity.manager_full_name }}</td>
                <td>{{ opportunity.stage }}</td>
                <td><router-link :to="{name: 'opportunity-details', params: { uuid: opportunity.uuid } }">Details</router-link></td>
              </tr>
            </template>
          </table-helper>
        </div>
      </div>

      <div v-else-if="$user_type == 'admin' || $user_type == 'super_admin'">
          Hi Admin
      </div>
      <div v-else-if="$user_type == 'manager'">
          Hi Manager
      </div>

      <div v-else-if="$user_type == 'member'">
          Hi Member
      </div>

  </div>
</template>
  
<script>
import TableHelper from './helpers/TableHelper.vue';
export default {
  components: {
        "table-helper": TableHelper,
  },
  data() {
    return {
      userType: this.$user_type,
      opportunities: [],
    };
  },
  created() {
    if (this.userType === 'agent') {
      this.getAgentOpportunities();
    }
  },
  mounted() {
    console.log('Name:', this.$user_full_name);
  },
  methods: {
    async getAgentOpportunities(){
        await this.$axios.get('/deal/opportunity/agent_opportunities/')
        .then(response => {
          this.opportunities = response.data
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        }) 
          
    },
  },
}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
  