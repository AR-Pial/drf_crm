<template>
<div>
	<div v-if="opportunity">

    <div class="card mx-2 mx-lg-5 my-5 shadow">
      <h5 class="card-header bg-secondary text-white text-start">Overview</h5>
      <div class="card-body">
        <p class="text-muted text-dark text-start "> Opportunity Name:  <span class="badge bg-secondary px-2 py-1">{{ opportunity.name }}</span><a class="ms-2" href="#">edit</a></p>
        <p class="text-muted text-dark text-start "> Manager Name:  <span class="badge bg-secondary px-2 py-1">{{ opportunity.manager_full_name }}</span> <a class="ms-2" href="#">edit</a></p>
        <p class="text-muted text-dark text-start "> Agent Name:  <span class="badge bg-secondary px-2 py-1">{{ opportunity.agent_full_name }}</span> <a class="ms-2" href="#">edit</a></p>   
        <p class="text-muted text-dark text-start "> Company Name:  <span class="badge bg-secondary px-2 py-1">{{ opportunity.company_name }}</span> <a class="ms-2" href="#">edit</a></p>
        <p class="text-muted text-dark text-start " > Stage:  <span class="badge bg-secondary px-2 py-1">{{ opportunity.stage }}</span> <a class="ms-2" href="#">edit</a></p>        
      </div>
    </div>

    <div v-if="opportunity.project_details" class="card mx-2 mx-lg-5 my-5 shadow">
      <h5 class="card-header bg-secondary text-white text-start d-flex align-items-center">       
        Project Details
        <a class="text-white ms-auto" href="">Edit</a>
      </h5>
      <div class="card-body">
        <p class="text-muted text-dark text-start " style="white-space: pre-wrap;"> {{ opportunity.project_details }}</p>        
      </div>
    </div>

    <div v-if="opportunity.company_details" class="card mx-2 mx-lg-5 my-5 shadow">
      <h5 class="card-header bg-secondary text-white text-start d-flex align-items-center">       
        Company Details
        <a class="text-white ms-auto" href="">Edit</a>
      </h5>
      <div class="card-body">
        <p class="text-muted text-dark text-start " style="white-space: pre-wrap;"> {{ opportunity.company_details }}</p>        
      </div>
    </div>

    <div v-if="opportunity.contact_details" class="card mx-2 mx-lg-5 my-5 shadow">
      <h5 class="card-header bg-secondary text-white text-start d-flex align-items-center">       
        Contact Details
        <a class="text-white ms-auto" href="">Edit</a>
      </h5>
      <div class="card-body">
        <p class="text-muted text-dark text-start " style="white-space: pre-wrap;"> {{ opportunity.contact_details }}</p>        
      </div>
    </div>

    <div v-if="opportunity.additional_info" class="card mx-2 mx-lg-5 my-5 shadow">
      <h5 class="card-header bg-secondary text-white text-start d-flex align-items-center">       
        Additional Info
        <a class="text-white ms-auto" href="">Edit</a>
      </h5>
      <div class="card-body">
        <p class="text-muted text-dark text-start " style="white-space: pre-wrap;"> {{ opportunity.additional_info }}</p>        
      </div>
    </div>

  </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      opportunity: null,
    };
  },
  created() {
    const uuid = this.$route.params.uuid;
    axios.get(`/deal/opportunity/${uuid}/`)
      .then(response => {
		console.log(response.data)
        this.opportunity = response.data;
      })
      .catch(error => {
        console.error('Error fetching opportunity details:', error);
      });
  },
};


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
	