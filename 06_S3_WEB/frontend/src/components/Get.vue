<template>

    <h3 class="mt-5"> Get ~ S3のファイル内容取得 ~ </h3>

    <!-- ファイルの名前入力 -->
    <div class="row g-3 align-items-center">
      <div class="col-2">
        <label for="inputPassword6" class="col-form-label"> File Name </label>
      </div>
      <div class="col-10">
        <input v-model="file_name" type="text" class="form-control mb-2" id="inputPassword6" placeholder="file_name">
      </div>
    </div>
    
    <!-- presigned url 取得ボタン -->
    <div class="d-grid gap-2 mt-2">
            <button @click="getFileContent" class="btn btn-primary btn-block py-1"> Get Image File </button>
    </div>

    <!-- 内容表示 -->
    <template class="card mt-5" v-if="presigned_url">
      <div class="card-header">
        <h3> {{ file_name }} </h3>
      </div>
      <div class="card-body">
        <img :src="presigned_url" class="img-fluid" alt="選択された画像" />
      </div>
    </template>

  </template>
  
  <script>
  
  export default {
    name: 'App',
    data() {
      return {
        file_name: "",
        imageSrc: '',
        presigned_url: '',
      }
    },
    methods: {
      async getFileContent() {
        this.presigned_url = await this.$store.dispatch('getPresigned', 
            { object_key: this.file_name, request_type: 'get_object' }
        )
      },
    },
  };
  </script>
  