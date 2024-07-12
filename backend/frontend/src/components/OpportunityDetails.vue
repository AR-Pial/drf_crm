<template>
<div>
  <div v-if="opportunity">

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

  

  </div>
</div>
</template>

<script>
import EditableBadgeField from './fields/EditableBadgeField.vue';
import EditableBadgeSelect from './fields/EditableBadgeSelect.vue';
import EditableCardField from './fields/EditableCardField.vue';
export default {
  components: {
    EditableBadgeField,
    EditableBadgeSelect,
    EditableCardField
  },
  data() {
    return {
      opportunity: null,
    };
  },
  created() {
    const uuid = this.$route.params.uuid;
    this.$axios.get(`/deal/opportunity/${uuid}/`)
      .then(response => {
        console.log(response.data)
        this.opportunity = response.data;
        console.log(this.opportunity)
      })
      .catch(error => {
        console.error('Error fetching opportunity details:', error);
      });
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
  