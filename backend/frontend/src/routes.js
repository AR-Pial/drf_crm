import { createRouter, createWebHistory } from 'vue-router';
import DashboardPage from './components/DashboardPage.vue';
import OpportunityApp from './components/OpportunityApp.vue';
import OpportunityDetails from './components/OpportunityDetails.vue';


const routes = [
  { path: '/',name: 'dashboard',component: DashboardPage },
  { path: '/deal/opportunity', name: 'opportunity', component: OpportunityApp},
  { path: '/deal/opportunity/details/:uuid', name: 'opportunity-details', component: OpportunityDetails},
 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;