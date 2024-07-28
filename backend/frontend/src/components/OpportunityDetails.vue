<template>
<div>
  <div v-if="opportunity">

    <div class="mx-2 mx-lg-5 my-3">
      <h3 class="py-2 py-lg-3">Opportunity Pipeline</h3>
        <div class="row">
            <div class="col">
                <div class="progress" style="height: 30px !important;">
                    <div class="progress-bar bg-secondary" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Assigned</div>
                    <div class="progress-bar bg-secondary bg-info" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Proposal</div>
                    <div class="progress-bar bg-secondary" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Negotiation</div>
                    <div class="progress-bar bg-secondary" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Lead</div>
                </div>
            </div>
        </div>
    </div>

    <div class="card mx-2 mx-lg-5 my-5 shadow">
      <h5 class="card-header bg-secondary text-white text-start">Overview</h5>
      <div class="card-body">
        <EditableBadgeField label="Opportunity Name" :value="opportunity.name" @update:value="updateOpportunityField"
        opportunityFieldname="name"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"    
        /> 
        <EditableBadgeSelect label="Manager Name" :value="opportunity.manager_user_id" :valueName="opportunity.manager_full_name" 
        @update:value="updateOpportunityField" :optionUrl="`/api/managers`" opportunityFieldname="manager" fieldName="manager_full_name" :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
        />

        <EditableBadgeSelect label="Agent Name" :value="opportunity.agent_user_id" :valueName="opportunity.agent_full_name" 
        @update:value="updateOpportunityField" :optionUrl="`/api/agents`" opportunityFieldname="agent" fieldName="agent_full_name" :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
        />

        <!-- <EditableBadgeSelect label="Agent Name" :valueName="opportunity.agent_full_name" /> -->
        <EditableBadgeField label="Company Name"  :value="opportunity.company_name" @update:value="updateOpportunityField"
        opportunityFieldname="company_name"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"/>
        <EditableBadgeSelect label="Stage" :value="opportunity.stage" :valueName="opportunity.stage" 
        @update:value="updateOpportunityField" opportunityFieldname="stage" fieldName="stage" :editUrl="`/deal/opportunity/${opportunity.uuid}/`" />      
      </div>
    </div>

    <EditableCardField fieldTitle="Opportunity Details" :fieldValue="opportunity.opportunity_details" @update:fieldValue="updateOpportunityField"
      opportunityFieldname="opportunity_details"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
    />

    <EditableCardField fieldTitle="Company Details" :fieldValue="opportunity.company_details" @update:fieldValue="updateOpportunityField"
      opportunityFieldname="company_details"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
    />

    <EditableCardField fieldTitle="Contact Details" :fieldValue="opportunity.contact_details" @update:fieldValue="updateOpportunityField"
      opportunityFieldname="contact_details"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
    />

    <EditableCardField fieldTitle="Additional Info" :fieldValue="opportunity.additional_info" @update:fieldValue="updateOpportunityField"
      opportunityFieldname="additional_info"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
    />

    <div class="mb-3 mb-lg-5">
      <h4>Documents</h4>

      <div class="mb-3 d-flex flex-row flex-wrap">
          <div class="text-start mt-1"><small>Files: </small></div>
          <div class="text-start"  v-for="file in files" :key="file.id"> 
            <span class="badge bg-info text-dark mx-1 my-1">{{ file.document.split('/').pop() }} 
              <button type="button"  class="btn-close" aria-label="Close" v-if="file.document" @click="deleteFile(file.id)"></button>
            </span> 
          </div>
      </div>  
    </div>

  </div>
</div>
</template>

<script>
import EditableBadgeField from './fields/EditableBadgeField.vue';
import EditableBadgeSelect from './fields/EditableBadgeSelect.vue';
import EditableCardField from './fields/EditableCardField.vue';
import getDataMixin from '@/mixins/getDataMixin';
export default {
  mixins: [getDataMixin],
  components: {
    EditableBadgeField,
    EditableBadgeSelect,
    EditableCardField
  },
  data() {
    return {
      opportunity: null,
      files: [],
    };
  },
  async  created() {
    const uuid = this.$route.params.uuid;
    // this.$axios.get(`/deal/opportunity/${uuid}/`)
    //   .then(response => {
    //     console.log(response.data)
    //     this.opportunity = response.data;
    //     console.log(this.opportunity)
    //   })
    //   .catch(error => {
    //     console.error('Error fetching opportunity details:', error);
    //   });
    const opportunityUrl = `/deal/opportunity/${uuid}/`;

  try {
    // Fetch the opportunity details
    this.opportunity = await this.fetchData(opportunityUrl);

    // Construct the URL for fetching files based on opportunity details
    const filesUrl = `/deal/opportunity_documents/${uuid}/get_opportunity_documents/`;

    // Fetch the files
    this.files = await this.fetchData(filesUrl);
  } catch (error) {
    this.error = error;
    console.error('Error fetching data:', error);
  }
  },
    methods: {
    updateOpportunityField(newValue,fieldName,valueName=null) {
      console.log(fieldName)
      if(valueName){
        console.log(valueName)
        this.opportunity[fieldName] = valueName;
      }
      else{
        this.opportunity[fieldName] = newValue;
      }

    },
  },
};


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
  