import axios from 'axios'

const instance = axios.create();

instance.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
instance.defaults.withCredentials = true;

instance.defaults.xsrfCookieName = "csrftoken"
instance.defaults.xsrfHeaderName = "X-CSRFToken"

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