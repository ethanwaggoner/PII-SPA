<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/store'

const authStore = useAuthStore()
const router = useRouter()


const email = ref('')
const password = ref('')

const authenticate = async (event) => {
  event.preventDefault()

  await authStore.login({
    email: email.value,
    password: password.value
  })

  if (authStore.$state.is_authenticated) {
    await router.push('/overview')
  }

}
</script>
<template>
  <div id="login" class="d-flex align-items-center justify-content-center vh-100">
    <form @submit="authenticate">
    <div class="login-container">
      <h1>PII Sign In</h1>

      <div class="form-group">
        <input v-model="email" type="text" class="form-control" placeholder="Email">
      </div>
      <div class="form-group">
        <input v-model="password" type="password" class="form-control" placeholder="Password">
      </div>
        <button class="btn login-button" type="submit">Sign in</button>
      <div class="or-container d-flex justify-content-center align-items-center">
        <span>or</span>
      </div>
      <button class="btn microsoft-login-button" type="submit">Sign in with Microsoft</button>
      <i class="bi bi-microsoft"></i>
      </div>
    </form>
  </div>
</template>

<style scoped>

#login {
  background: #1e293b;;
  font-family: Arial, sans-serif;
  overflow: hidden;
}

h1 {
  align-self: center;
}

i {
  background-color: white;
}

label {

}

.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
  padding: 30px;
  border: 3px solid #5A6D7C;
  border-radius: 10px;
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C, 0 0 8px #5A6D7C, 0 0 12px #5A6D7C;
  background: linear-gradient(180deg, #10142c, #252c48);
  color: white;
}

.or-container {
  color: white;
}

.btn {
  background: none;
  border: 2px solid #5A6D7C;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  font-size: 24px;
  padding: 10px 20px;
  transition: background-color 0.3s ease, color 0.3s ease, border 0.3s ease;
  box-shadow: 0 0 2px #5A6D7C, 0 0 4px #5A6D7C;
}

.btn:hover {
  background-color: rgba(90, 109, 124, 0.1);
  color: #5A6D7C;
  border-color: white;
  box-shadow: 0 0 5px #5A6D7C, 0 0 15px #5A6D7C, 0 0 25px #5A6D7C, 0 0 35px #5A6D7C;
}

.form-control {
  width: 300px;
}

</style>