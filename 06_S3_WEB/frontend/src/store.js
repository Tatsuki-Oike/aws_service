import { createStore } from 'vuex'
import axios from 'axios'

export const store = createStore({
    state() {
        return {
            api_url: import.meta.env.API_URL,
            presigned_api_url: `${import.meta.env.API_URL}/presigned`,
        }
    },
    actions: {
        async getPresigned(context, {object_key, request_type}) {

            // クエリデータ作成
            const QUERY_DATA = {
              'object_key': object_key,
              "request_type": request_type
            };

            // バックエンドからpresigned url取得
            try {
              const response = await axios.get(context.state.presigned_api_url, {
                params: QUERY_DATA
              });
              const parsedResponse = JSON.parse(response.data);
              const presigned_url = parsedResponse.presigned_url;
        
              return presigned_url;
            } catch (error) {
              throw new Error("Presigned URLの取得に失敗しました");
            }
        }
    }        
})