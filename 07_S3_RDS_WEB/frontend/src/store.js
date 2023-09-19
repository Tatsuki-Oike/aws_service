import { createStore } from 'vuex'

export const store = createStore({
    state() {
        return {
            api_url: import.meta.env.API_URL,
            presigned_api_url: `${import.meta.env.API_URL}/presigned`,
        }
    },
})