import { createApp } from 'vue'
import App from './App.vue'
import router from './routes'; // Import the router instance
import axios from './axios'

const app = createApp(App);
app.use(router); // Use the router


await axios.get('/api/get-auth-token/')
    .then(response => {
        const authToken = response.data.token;
        localStorage.setItem('authToken', authToken);
        app.config.globalProperties.$authToken = authToken;
    })
    .catch(error => {
        console.error('Error fetching auth token:', error);
    });

await axios.get('/api/get_user_profile/')
    .then(response => {
        const user_full_name = response.data.full_name;
        const user_type = response.data.user_type;
		localStorage.setItem('user_full_name', user_full_name);
		localStorage.setItem('user_type', user_type);
		app.config.globalProperties.$user_full_name = user_full_name;
		app.config.globalProperties.$user_type = user_type;

	}).catch(error => {
        console.error('Error fetching user profile:', error);
        // Handle the error appropriately
    });
// Add the token and name to the global properties
// app.config.globalProperties.$authToken = authToken;
app.config.globalProperties.$axios = axios;
app.mount('#app');


