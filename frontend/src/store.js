import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('authStore', {
    state: () => ({
        token: null,
        user_id: null,
        is_authenticated: false,
    }),
    actions: {
        async login({email, password}) {
            const response = await axios.post('http://127.0.0.1:5001/auth/', {
                email: email,
                password: password
            })
            if (response.data.success) {
                this.token = response.data.token
                this.user_id = response.data.user_id
                this.is_authenticated = response.data.is_authenticated
                axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`

            }
        },

        async logout() {
            const response = await axios.post('http://127.0.0.1:5001/deauth/', {
                token: this.token,
            })
            if (response.data.success) {
                this.token = null
                this.user_id = null
                this.is_authenticated = false
                axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`
            }
        }
    }
})