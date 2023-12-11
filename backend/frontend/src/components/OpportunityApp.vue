<template>
  <div>
    <div class="col-11 col-lg-10 mx-auto my-3">
      <table-helper :add-button-name="addButtonName">
        <template v-slot:table-name>
            Opportunities
        </template>
        <template v-slot:header>
          <th>Name</th>
          <th>Company Name</th>
          <th>Stage</th>
          <th>Details</th>
          <th>Action</th>
        </template>

        <template v-slot:body>
          <tr v-for="opportunity in opportunities" :key="opportunity.id">
            <td>{{ opportunity.name }}</td>
            <td>{{ opportunity.company_name }}</td>
            <td>{{ opportunity.stage }}</td>
            <td><router-link :to="{name: 'opportunity-details', params: { uuid: opportunity.uuid } }">Details</router-link></td>
            <td>
              
              <a href="" @click="opportunity_edit(opportunity.uuid)" data-bs-toggle="modal" data-bs-target="#editModal">Edit</a> /
              <a href="#">Delete</a>
            
            </td>
          </tr>
        </template>
      </table-helper>
      <modal-helper ref="modalHelper" :modal-header-name="modalHeader" >
        <template v-slot:body>
          <form-helper @submitForm="submitForm">
              <template v-slot:body>
                
                <div class="mb-3 row">
                  <div class="col-12 col-lg-6">
                    <div class="text-start pb-1" >Opportunity Name:</div>
                    <input class="form-control" type="text" v-model="opportunity.name" id="name" name="name" />
                  </div>
                  <div class="col-12 col-lg-6">
                    <div class="text-start pb-1">Company Name:</div>
                    <input class="form-control" type="text" v-model="opportunity.company_name" id="name" name="company_name" />      
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
                    <div class="text-start pb-1">Opportunity Details:</div>
                    <textarea class="form-control" rows="4" v-model="opportunity.opportunity_details" id="opportunity_details" name="opportunity_details"></textarea>      
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
                      <label class="btn btn-primary text-start py-1 px-2"  for="fileInput">
                        <svg xmlns="http://www.w3.org/2000/svg"  height="1.15em" viewBox="0 0 448 512" style="fill: white;">
                          <path d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"/>
                        </svg> <span class="px-1"> Add Files</span>
                      </label> 
                    </div> 
                  </div>
                </div>
                <div class="mb-3 d-flex flex-row flex-wrap">             
                  <div class="text-start mt-1"><small>Uploaded Files: </small></div>
                  <div class="text-start"  v-for="(file, index) in selectedFiles" :key="file.name"> 
                    <span class="badge bg-info text-dark mx-1 my-1">{{ file.name }} 
                      <button type="button"  class="btn-close" aria-label="Close" @click="removeFile(index)"></button>
                    </span> 
                  </div>
                </div>               
              </template>
          </form-helper>
        </template>
      </modal-helper>

      <edit-modal-helper ref="editModalHelper" :edit-modal-header-name="editModalHelper">
        <template v-slot:body>
          <form-helper @editSubmitForm="editSubmitForm">
              <template v-slot:body>
                <div class="mb-3 row">
 
                    <div class="col-12 col-lg-6"> 
                      <div class="text-start pb-1" >Opportunity Name:</div>
                      <input class="form-control" type="text" v-model="opportunity.name" id="name" name="name" />
                    </div>
                </div>
                <div class="mb-3 row">
                  <div class="col-12 col-lg-6"> 
                      <div class="text-start pb-1" >Company Name:</div>
                      <input class="form-control" type="text" v-model="opportunity.company_name" id="name" name="company_name" />
                    </div>
                    <div class="col-12 col-md-6">
                      <div class="text-start pb-1" >Stage:</div>
                      <select class="form-select" v-model="opportunity.stage" id="manager" name="manager">
                        <option value="Unassigned">Unassigned</option>
                        <option value="Assigned">Assigned</option>
                        <option value="Lead">Lead</option>
                        <option value="Unsuccessful">Unsuccessful</option>
                        <option value="Successful">Successful</option>                   
                      </select>
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
                    <div class="text-start pb-1">Opportunity Details:</div>
                    <textarea class="form-control" rows="4" v-model="opportunity.opportunity_details" id="opportunity_details" name="opportunity_details"></textarea>      
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
                      <label class="btn btn-primary text-start py-1 px-2"  for="fileInput">
                        <svg xmlns="http://www.w3.org/2000/svg"  height="1.15em" viewBox="0 0 448 512" style="fill: white;">
                          <path d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"/>
                        </svg> <span class="px-1"> Add Files</span>
                      </label> 
                    </div> 
                  </div>
                </div>
                <div class="mb-3 d-flex flex-row flex-wrap">
                  <div class="text-start mt-1"><small>Files: </small></div>
                  <div class="text-start"  v-for="file in files" :key="file.id"> 
                    <span class="badge bg-info text-dark mx-1 my-1">{{ file.document.split('/').pop() }} 
                      <button type="button"  class="btn-close" aria-label="Close" v-if="file.document" @click="deleteFile(file.id)"></button>
                    </span> 
                  </div>
                  <div class="text-start"  v-for="(file, index) in selectedFiles" :key="file.name"> 
                    <span class="badge bg-info text-dark mx-1 my-1">{{ file.name }} 
                      <button type="button"  class="btn-close" aria-label="Close" @click="removeFile(index)"></button>
                    </span> 
                  </div>
                </div>              
              </template>
          </form-helper>
        </template>
      </edit-modal-helper>
    </div>
  </div>
</template>
  
  <script>
  import TableHelper from './helpers/TableHelper.vue';
  import ModalHelper from './helpers/ModalHelper.vue';
  import EditModalHelper from './helpers/EditModalHelper.vue';
  import FormHelper from './helpers/FormHelper.vue';
  export default {
    components: {
        "table-helper": TableHelper,
        "modal-helper": ModalHelper,
        "edit-modal-helper": EditModalHelper,
        "form-helper": FormHelper,
    },
    data(){
      return {
        addButtonName: "Create Opportunity",
        modalHeader: "Create Opportunity",
        editModalHelper: "Edit Opportunity",
        opportunities: [],
        opportunity: {
            name: '',
            company_name: '',
            stage: '',
            manager: '',
            agent: '',
            company_details: '',
            opportunity_details: '',
            contact_details: '',
            additional_info: '',           
        },
        agents: [],    
        managers: [],
        selectedFiles: [],
        files: [],
        opportunity_uuid: ''
        // isModalOpen: true,
      }
    },
    methods: {
      async deleteFile(fileId) {
        try {
          const response = await this.$axios.delete(`/opportunity_documents/${fileId}/`);
          // If the deletion is successful, remove the file from the local data
          if (response.status === 204) {
            this.files = this.files.filter(file => file.id !== fileId);
            console.log("ok delete")
          }
        } catch (error) {
          console.error('Error deleting file:', error);
        }
      },
      handleFileChange(event) {
        this.selectedFiles.push(...event.target.files);
        console.log(this.selectedFiles)
        event.target.value = ''
        
      },

      removeFile(index) {
        this.selectedFiles.splice(index, 1);
      },
      closeModal() {
        this.$refs.modalHelper.closeModal(); // Call the closeModal method in modal-helper
      },
      closeEditModal() {
        this.$refs.editModalHelper.closeModal(); // Call the closeModal method in modal-helper
      },

      async submitForm() {

        var formData = new FormData();
        // Append form fields
        formData.append('name', this.opportunity.name);
        formData.append('company_name', this.opportunity.company_name);
        formData.append('manager', this.opportunity.manager);
        formData.append('agent', this.opportunity.agent);
        formData.append('company_details', this.opportunity.company_details);
        formData.append('opportunity_details', this.opportunity.opportunity_details);
        formData.append('contact_details', this.opportunity.contact_details);
        formData.append('additional_info', this.opportunity.additional_info);

                     
        this.$axios.post('/deal/opportunity/', formData)
          .then(response => {
            console.log('Opportunity created:', response.data);

            if(this.selectedFiles.length === 0){
              this.closeModal();
              this.getOpportunities();             
            }

            else{
              var documentData = new FormData();
              documentData.append('opportunity', response.data.id);
              for (const file of this.selectedFiles) {
                documentData.append('files[]', file);
              }
                      
              this.$axios.post('/deal/opportunity_documents/', documentData, {
              headers: {
                'Content-Type': 'multipart/form-data',
                }
              })
              .then(response => {
                console.log('File created:', response.data);
                this.closeModal();
                this.getOpportunities();
                this.selectedFiles = ""              
              }).catch(error => {
                console.error('Error creating opportunity documents:', error);
              });
              }
          
          })
          .catch(error => {
            console.error('Error creating opportunity:', error);
          });
                
      },

      async opportunity_edit(opportunityUUId) {
        console.log("opportunity_id = " + opportunityUUId)
        this.opportunity_uuid = opportunityUUId
        this.$axios.get(`/deal/opportunity/${opportunityUUId}/`)
          .then(response => {
            // Handle the response here. The specific opportunity will be in response.data.
            // const opportunityss = response.data;
            console.log(response.data)
            this.opportunity.name = response.data.name
            this.opportunity.company_name = response.data.company_name
            this.opportunity.stage = response.data.stage
            this.opportunity.manager = response.data.manager
            this.opportunity.agent = response.data.agent
            this.opportunity.company_details = response.data.company_details
            this.opportunity.contact_details = response.data.contact_details
            this.opportunity.opportunity_details = response.data.opportunity_details
            this.opportunity.additional_info = response.data.additional_info

            this.$axios.get(`/deal/opportunity_documents/${opportunityUUId}/get_opportunity_documents/`)
              .then(response => {
                console.log(response.data)
                this.files = response.data;
                console.log(this.files)
              }).catch(error => {
                // Handle any errors that occur during the request.
                console.error(error);
              });

          })
          .catch(error => {
            // Handle any errors that occur during the request.
            console.error(error);
          });
      },

      async editSubmitForm(){
        const editedOpportunityData = {
        name: this.opportunity.name,
        company_name: this.opportunity.company_name,
        stage: this.opportunity.stage,
        manager: this.opportunity.manager,
        agent: this.opportunity.agent,
        company_details: this.opportunity.company_details,
        contact_details: this.opportunity.contact_details,
        opportunity_details: this.opportunity.opportunity_details,
        additional_info: this.opportunity.additional_info, 
        }
        let uuid = this.opportunity_uuid
        await this.$axios.put(`/deal/opportunity/${uuid}/`,editedOpportunityData) 
        .then(response => {
          console.log(response.data)
          
          if(this.selectedFiles.length === 0){
              this.closeEditModal();
              this.getOpportunities();             
            }

            else{
              var documentData = new FormData();
              documentData.append('opportunity', response.data.id);
              for (const file of this.selectedFiles) {
                documentData.append('files[]', file);
              }
                      
              this.$axios.post('/deal/opportunity_documents/', documentData, {
              headers: {
                'Content-Type': 'multipart/form-data',
                }
              })
              .then(response => {
                console.log('File created:', response.data);
                this.closeEditModal();
                this.getOpportunities();
                this.selectedFiles = ""              
              }).catch(error => {
                console.error('Error creating opportunity documents:', error);
              });
              } 
        })
        .catch(error => {
          console.log(error)
        }) 

      },
      async getOpportunities(){
        
        await this.$axios.get('/deal/opportunity/')
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
          const response = await this.$axios.get('/api/agents'); // Replace with your actual API endpoint
          this.agents = response.data;
          console.log(this.agents)
        } catch (error) {
          console.error('Error fetching agents:', error);
        }
      },
      async fetchManagers() {
          try {
            const response = await this.$axios.get('/api/managers'); // Replace with your actual API endpoint
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
.badge .btn-close {
            padding-top: 3px;
            font-size: 0.65rem;
        }
  </style>
  