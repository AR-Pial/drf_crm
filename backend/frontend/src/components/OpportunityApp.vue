<template>
	<div>
		<div class="col-11 col-lg-10 mx-auto my-3">
      <table-helper :add-button-name="addButtonName">
        <template v-slot:table-name>
            Opportunities
        </template>
        <template v-slot:header>
          <th>Name</th>
          <th>Stage</th>
          <th>Action</th>
        </template>

        <template v-slot:body>
          <tr v-for="opportunity in opportunities" :key="opportunity.id">
            <td>{{ opportunity.name }}</td>
            <td>{{ opportunity.stage }}</td>
            <td><a href="#">Details</a></td>
          </tr>
        </template>
      </table-helper>
      <modal-helper :modal-header-name="modalHeader">
        <template v-slot:body>
          <form-helper @submitForm="submitForm">
              <template v-slot:body>
                <div class="mb-3 row">
                  <div class="col-12 col-md-6">
                    <div class="text-start pb-1" >Opportunity Name:</div>
                    <input class="form-control" type="text" v-model="opportunity.name" id="name" name="name" />
                  </div>
                </div>
                <div class="mb-3 row">

                  <div class="col-12 col-md-6">
                    <div class="text-start pb-1">Manager:</div>
                    <select class="form-select" v-model="opportunity.manager" id="manager" name="manager">
                      <option value="">Select a manager</option>
                      <option v-for="manager in managers" :key="manager.id" :value="manager.id">{{ manager.first_name }} {{ manager.last_name }}</option>
                    </select>
                  </div>

                  <div class="col-12 col-md-6">
                    <div class="text-start pb-1">Agent:</div>
                    <select class="form-select" v-model="opportunity.agent" id="agent" name="agent">
                      <option value="">Select an agent</option>
                      <option v-for="agent in agents" :key="agent.id" :value="agent.id">{{ agent.first_name  }} {{ agent.last_name }}</option>
                    </select>
                  </div>
                </div>

                <div class="row mb-3">
                  <div class="col-12 col-lg-6">
                    <div class="text-start pb-1">Company Details:</div>
                    <textarea class="form-control" rows="4" v-model="opportunity.company_details" id="company_details" name="company_details"></textarea>      
                  </div>
                  <div class="col-12 col-lg-6">
                    <div class="text-start pb-1">Project Details:</div>
                    <textarea class="form-control" rows="4" v-model="opportunity.project_details" id="project_details" name="project_details"></textarea>      
                  </div>
                </div>

                <div class="row mb-3">
                  <div class="col-12 col-lg-6">
                    <div class="text-start pb-1">Contact Details:</div>
                    <textarea class="form-control" rows="4" v-model="opportunity.contact_details" id="contact_details" name="contact_details"></textarea>      
                  </div>
                  <div class="col-12 col-lg-6">
                    <div class="text-start pb-1">Additional Details:</div>
                    <textarea class="form-control" rows="4" v-model="opportunity.additional_info" id="additional_info" name="additional_info"></textarea>      
                  </div>
                </div>
                <div class="row mb-3">
                  <div class="col-12 col-lg-6">
                    <input class="d-none form-control" id="fileInput" type="file" ref="fileInput" multiple @change="handleFileChange">
                    <div class="text-start ">
                      <label class="btn btn-primary text-start p-2"  for="fileInput">
                        <svg xmlns="http://www.w3.org/2000/svg"  height="1.15em" viewBox="0 0 448 512" style="fill: white;">
                          <path d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"/>
                        </svg> <span class="px-1"> Add Files</span>
                      </label> 
                    </div> 
                  </div>
                </div>
                <div>
                  <h3>Uploaded Files:</h3>
                  <ul>
                    <li  v-for="file in selectedFiles" :key="file.name">{{ file.name }}</li>
                  </ul>
                </div>
              </template>
          </form-helper>
        </template>
      </modal-helper>

       
      

    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  import TableHelper from './helpers/TableHelper.vue';
  import ModalHelper from './helpers/ModalHelper.vue';
  import FormHelper from './helpers/FormHelper.vue';
  export default {
    components: {
        "table-helper": TableHelper,
        "modal-helper": ModalHelper,
        "form-helper": FormHelper,
    },
    data(){
      return {
        addButtonName: "Create Opportunity",
        modalHeader: "Create Opportunity",
        opportunities: [],
        opportunity: {
            name: '',
            manager: '',
            agent: '',
            company_details: '',
            project_details: '',
            contact_details: '',
            additional_info: '',
            
        },
        agents: [],    
        managers: [],
        documents: [],
        selectedFiles: []
      }
    },
    methods: {
      handleFileChange(event) {
        this.selectedFiles.push(...event.target.files);

        console.log(this.selectedFiles)
        event.target.value = ''
        
      },
      uploadFiles() {

      },
      submitForm() {
        // console.log("Form submitted")
        this.documents = this.selectedFiles.slice();
      
        console.log('Documents :'+ this.documents);
      },
      async getOpportunities(){
        await axios.get('http://localhost:8000/deal/opportunity/')
        .then(response => {
          this.opportunities = response.data
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        }) 
          
      },
      async fetchAgents() {
        try {
          const response = await axios.get('http://localhost:8000/api/agents'); // Replace with your actual API endpoint
          this.agents = response.data;
          console.log(this.agents)
        } catch (error) {
          console.error('Error fetching agents:', error);
        }
      },
      async fetchManagers() {
          try {
            const response = await axios.get('http://localhost:8000/api/managers'); // Replace with your actual API endpoint
            this.managers = response.data;
            console.log(this.managers)
          } catch (error) {
            console.error('Error fetching managers:', error);
          }
      },

    },
    async mounted() {
      await this.getOpportunities(); 
      await this.fetchAgents();
      await this.fetchManagers();
    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

  </style>
  