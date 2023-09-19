import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import Upload from './components/Upload.vue'
import Get from './components/Get.vue'
import Delete from './components/Delete.vue'

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/upload',
            name: 'upload',
            component: Upload,
        },
        {
            path: '/get',
            name: 'get',
            component: Get,
        },
        {
            path: '/delete',
            name: 'delete',
            component: Delete,
        },
    ]
})