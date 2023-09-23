<template>

    <h3 class="mt-5">Get ~ S3のファイル消去 ~</h3>

    <!-- ファイルの名前入力 -->
    <div class="row g-3 align-items-center">
      <div class="col-2">
        <label for="inputPassword6" class="col-form-label">File Name</label>
      </div>
      <div class="col-10">
        <input v-model="file_name" type="text" class="form-control mb-2" id="inputPassword6" placeholder="file_name">
      </div>
    </div>
    
    <!-- 消去ボタン -->
    <div class="d-grid gap-2 mt-2">
      <button @click="deleteFileContent" class="btn btn-primary btn-block py-1">Delete Image File</button>
    </div>

  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'App',
    data() {
      return {
        file_name: "",
      }
    },
    methods: {
      async deleteFileContent() {
        try {
          
          const presigned_url = await this.$store.dispatch('getPresigned', 
              { object_key: this.file_name, request_type: 'delete_object' }
          )

          await axios.delete(presigned_url)
          console.log("SUCCESS");
        } catch (error) {
          console.error("FAIL: ", error);
        }
      },
      
    },
  };
  </script>
  