<template>

    <h3 class="mt-5"> Upload ~ S3に画像ファイルアップロード ~</h3>

    <!-- ファイルの名前入力 -->
    <div class="row g-3 align-items-center my-3">
        <div class="col-2">
        <label for="inputPassword6" class="col-form-label">File Name</label>
        </div>
        <div class="col-10">
        <input v-model="file_name" type="text" class="form-control mb-2" id="inputPassword6" placeholder="file_name">
        </div>
    </div>

    <!-- 画像アップロード -->
    <input class="form-control my-3" type="file" @change="onFileChange" accept=".jpg, .png" />
    <div class="d-grid gap-2 mt-3">
            <button @click="uploadImgFile" class="btn btn-primary btn-block py-1">Upload Image File</button>
    </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'App',
    data() {
        return {
        file_content: "",
        file_name: "",
        selectedFile: null,
        }
    },
    methods: {
        onFileChange(event) {
            this.selectedFile = event.target.files[0]; 
        },
        async uploadImgFile() {

            if (!this.selectedFile) {
                console.error('ファイルが選択されていません');
            }

            try {

                // presigned url 取得
                const presigned_url = await this.$store.dispatch('getPresigned', 
                    { object_key: this.file_name, request_type: 'put_object' }
                )
                
                // ファイルのアップロード
                await axios.put(presigned_url, this.selectedFile, {
                    headers: {
                        'Content-Type': this.selectedFile.type,
                    },
                });
                
                this.file_name = ""
                console.log('SUCCESS');
            } catch (error) {
                console.error('FAIL:', error);
            }
        },
    },
};
</script>
