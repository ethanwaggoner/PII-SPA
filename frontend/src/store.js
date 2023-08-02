import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('authStore', {
    state: () => ({
        token: null,
        user: null,
        success: false
    }),
    actions: {
        async login({email, password}) {
            const response = await axios.post('http://127.0.0.1:5001/auth', {
                email,
                password
            })
            if (response.data.success) {
                this.token = response.data.token
                this.user = response.data.user
                axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
            }
        }
    }
})