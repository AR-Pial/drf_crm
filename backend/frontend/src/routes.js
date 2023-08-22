import { createRouter, createWebHistory } from 'vue-router';
import DashboardPage from './components/DashboardPage.vue';
import OpportunityApp from './components/OpportunityApp.vue';

const routes = [
  { path: '/',name: 'dashboard',component: DashboardPage },
  { path: '/deal/opportunity', name: 'opportunity', component: OpportunityApp},
  { path: '/registration', name: 'registration'},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;