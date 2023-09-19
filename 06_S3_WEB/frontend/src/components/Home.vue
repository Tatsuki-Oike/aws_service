<template>

  <h3 class="mt-5"> Home ~ S3のファイル一覧 ~ </h3>
  
  <template v-for="file in file_list">
    <ul class="list-group">
      <li class="list-group-item"> {{ file }} </li>
    </ul>
  </template>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      file_list: {}
    }
  },
  mounted() {
    axios
      .get(this.$store.state.api_url)
      .then(response => {
        const json_response = JSON.parse(response.data);
        this.file_list = json_response["file_list"]
        console.log("SUCCESS");
      })
      .catch(error => {
        this.response = error;
        console.log("FAIL: ", error);
      });
  },
}
</script>