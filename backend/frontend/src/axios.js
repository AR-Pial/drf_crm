import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL,  // Uses the root URL directly
});

instance.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
instance.defaults.withCredentials = true;
const authToken = localStorage.getItem('authToken');

instance.defaults.xsrfCookieName = "csrftoken"
instance.defaults.xsrfHeaderName = "X-CSRFToken"
if (authToken) {
  instance.defaults.headers.common['Authorization'] = `Token ${authToken}`;
}

instance.interceptors.response.use(
  (response) => {
    // Handle the response data if needed
    return response;
  },
  (error) => {
    // Handle any response errors
    if (error.response) {
      // The request was made and the server responded with a status code that is not in the range of 2xx
      // console.log(error.response.status);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('AxiosError:EmptyResponse', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('AxiosError:Setup', error.message);
    }
    return Promise.reject(error);
  }
);

export default instance