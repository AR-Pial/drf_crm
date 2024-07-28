// src/mixins/fetchDataMixin.js
export default {
	methods: {
	  async fetchData(url) {
		try {
		  const response = await this.$axios.get(url);
		  return response.data;
		} catch (error) {
		  console.error(error);
		  throw error;
		}
	  }
	}
  };
  