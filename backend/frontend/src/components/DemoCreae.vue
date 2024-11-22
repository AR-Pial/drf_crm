<template>
  <div>
    <h2>Create Post</h2>
    <form @submit.prevent="submitForm(endpoints.posts)">
      <div>
        <label for="title">Title:</label>
        <input v-model="formData.title" type="text" id="title" required />
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea v-model="formData.content" id="content" required></textarea>
      </div>
      <button type="submit">Create Post</button>
    </form>
    <div v-if="success" class="success">{{ success }}</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import formMixin from '@/mixins/formMixin';
import { endpoints } from '@/src/api';

export default {
  mixins: [formMixin],
  data() {
    return {
      formData: {
        title: '',
        content: '',
      },
    };
  },
};
</script>

<style scoped>
.success {
  color: green;
}
.error {
  color: red;
}
</style>
