<template>
<div>
  <div v-if="opportunity" class="mx-2 mx-lg-5 my-3">
      <h3 class="py-2 py-lg-3">Opportunity Pipeline</h3>
        <div class="row">
            <div class="col">
                <div class="progress rounded-0" style="height: 30px !important;">
                    <div class="progress-bar bg-secondary border-end border-4 fs-6" :class="opportunity.stage === 'Assigned' ? 'bg-info' : ''" role="progressbar" style="width: 20%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Assigned</div>
                    <div class="progress-bar bg-secondary border-end border-4 fs-6" :class="opportunity.stage === 'Proposal' ? 'bg-info' : ''" role="progressbar" style="width: 20%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                      <router-link class="text-white " :to="{name: 'proposal', params: { uuid: opp_uuid} }">Proposal</router-link>
                    </div>
                    <div class="progress-bar bg-secondary border-end border-4 fs-6" :class="opportunity.stage === 'Negotiation' ? 'bg-info' : ''" role="progressbar" style="width: 20%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Negotiation</div>
                    <div class="progress-bar bg-secondary border-end border-4 fs-6" :class="opportunity.stage === 'Lead' ? 'bg-info' : ''" role="progressbar" style="width: 20%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Lead</div>
                    <div class="progress-bar bg-secondary fs-6" :class="opportunity.stage === 'Successful' || opportunity.stage === 'Unsuccessful' ? 'bg-info' : ''" role="progressbar" style="width: 20%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">Result</div>
                </div>
            </div>
        </div>
    </div>

  <div class="mt-lg-4" v-if="opportunity">
    <h3 class="py-2 py-lg-3">Opportunity Details</h3>
    <div class="card mx-2 mx-lg-5 my-3 shadow">
      <h5 class="card-header bg-secondary text-white text-start">Overview</h5>
      <div class="card-body d-flex flex-column gap-3">
        <EditableBadgeField label="Opportunity Name" :value="opportunity.name" @update:value="updateOpportunityField"
        Fieldname="name"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"    
        /> 
        <EditableBadgeSelect label="Manager Name" :value="opportunity.manager_user_id" :valueName="opportunity.manager_full_name" 
        @update:value="updateOpportunityField" :optionUrl="`/api/managers`" Fieldname="manager" option_fieldName="manager_full_name" :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
        />

        <EditableBadgeSelect label="Agent Name" :value="opportunity.agent_user_id" :valueName="opportunity.agent_full_name" 
        @update:value="updateOpportunityField" :optionUrl="`/api/agents`" Fieldname="agent" option_fieldName="agent_full_name" :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
        />

        <!-- <EditableBadgeSelect label="Agent Name" :valueName="opportunity.agent_full_name" /> -->
        <EditableBadgeField label="Company Name"  :value="opportunity.company_name" @update:value="updateOpportunityField"
        Fieldname="company_name"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"/>
        <EditableBadgeSelect label="Stage" :value="opportunity.stage" :valueName="opportunity.stage" 
        @update:value="updateOpportunityField" Fieldname="stage" option_fieldName="stage" :editUrl="`/deal/opportunity/${opportunity.uuid}/`" />      
      </div>
    </div>
    <div class="mx-2 mx-lg-5 d-flex flex-column gap-4">
      <EditableCardField fieldTitle="Opportunity Details" :fieldValue="opportunity.opportunity_details" @update:fieldValue="updateOpportunityField"
        Fieldname="opportunity_details"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
      />

      <EditableCardField fieldTitle="Company Details" :fieldValue="opportunity.company_details" @update:fieldValue="updateOpportunityField"
        Fieldname="company_details"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
      />

      <EditableCardField fieldTitle="Contact Details" :fieldValue="opportunity.contact_details" @update:fieldValue="updateOpportunityField"
        Fieldname="contact_details"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
      />

      <EditableCardField fieldTitle="Additional Info" :fieldValue="opportunity.additional_info" @update:fieldValue="updateOpportunityField"
        Fieldname="additional_info"   :editUrl="`/deal/opportunity/${opportunity.uuid}/`"
      />
    </div>

    <div class="mb-3 mb-lg-5 mx-2 mx-lg-5 my-4">
      <div class="row mb-3">
          <div class="col-12 col-lg-6">
            <input class="d-none form-control" id="fileInput" type="file" ref="fileInput" multiple @change="handleFileChange">
            <div class="text-start ">
              <label class="btn btn-primary text-start py-1 px-2"  for="fileInput">
                <svg xmlns="http://www.w3.org/2000/svg"  height="1.15em" viewBox="0 0 448 512" style="fill: white;">
                  <path d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"/>
                </svg> <span class="px-1"> Add Files</span>
              </label> 
            </div> 
          </div>
        </div>
      <div class="mb-3 d-flex flex-row flex-wrap">

          <div class="text-start mt-1"><h5 class="me-2 mt-2">Files: </h5></div>
          <!-- <div class="text-start pe-3"  v-for="(file, index) in selectedFiles" :key="file.name"> 
              <span class="badge bg-info text-dark mx-0 px-0 row align-items-center py-2">
                <span class="fs-6 text-dark px-0 mx-2">{{ file.name }} </span>  
                <button type="button"  class="btn-close me-2" aria-label="Close" @click="removeFile(index)"></button>
              </span> 
          </div> -->
          <div class="text-start pe-3 my-2"  v-for="file in files" :key="file.id">
            <span class="badge bg-info text-dark mx-0 px-0 row align-items-center py-2"> 
              <a class="fs-6 text-dark px-0 mx-2" :href="file.document" download>{{ file.document.split('/').pop() }}</a>  
              <button type="button"  class="btn-close me-2" aria-label="Close" v-if="file.document" @click="deleteFile(file.id)"></button>
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
      selectedFiles: [],
      opp_uuid: null
    };
  },
  async  created() {
    this.opp_uuid = this.$route.params.uuid;
    // this.$axios.get(`/deal/opportunity/${uuid}/`)
    //   .then(response => {
    //     console.log(response.data)
    //     this.opportunity = response.data;
    //     console.log(this.opportunity)
    //   })
    //   .catch(error => {
    //     console.error('Error fetching opportunity details:', error);
    //   });
    const opportunityUrl = `/deal/opportunity/${this.opp_uuid}/`;

  try {
    // Fetch the opportunity details
    this.opportunity = await this.fetchData(opportunityUrl);
    console.log(this.opportunity)

    // Construct the URL for fetching files based on opportunity details
    const filesUrl = `/deal/opportunity_documents/${this.opp_uuid}/get_opportunity_documents/`;

    // Fetch the files
    this.files = await this.fetchData(filesUrl);
  } catch (error) {
    this.error = error;
    console.error('Error fetching data:', error);
  }
  },
  
    methods: {
      async deleteFile(fileId) {
        console.log("delete")
        try {
          const response = await this.$axios.delete(`/deal/opportunity_documents/${fileId}/`);
          // If the deletion is successful, remove the file from the local data
          if (response.status === 204) {
            console.log("delete done")
            this.files = this.files.filter(file => file.id !== fileId);
          }
        } catch (error) {
          console.error('Error deleting file:', error);
        }
      },
      getFileUrl(path) {
        return `${window.location.origin}/media/${path}`;
      },
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
      handleFileChange(event) {
        this.selectedFiles = Array.from(event.target.files);
        this.uploadFiles();
      },
      async uploadFiles() {
        const formData = new FormData();
        this.selectedFiles.forEach((file, index) => {
          formData.append(`files[]`, file);
        });
        formData.append('opportunity', this.opp_uuid);  // Assuming you have the opportunity UUID in your component
        console.log("opp_uuid : " + this.opp_uuid);

        try {
          const response = await this.$axios.post('/deal/opportunity_documents/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
          console.log('Files uploaded successfully', response.data);
          this.selectedFiles = []; 
          // Clear the files array after upload
          const filesUrl = `/deal/opportunity_documents/${this.opp_uuid}/get_opportunity_documents/`;
          this.files = await this.fetchData(filesUrl);
        } catch (error) {
          console.error('Error uploading files', error);
        }
      }
  },
};


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
  