<template>
  <div
    class="fixed inset-0 bg-opacity-50  bg-gradient-to-t from-sky-200 to-white flex items-center justify-center px-4">
    <div class="bg-white shadow-md rounded-lg p-8 max-w-sm w-full">
      <h2 class="text-2xl font-extrabold text-gray-600">Login</h2>
      <p class="text-sm font-normal text-gray-500 py-4">Please log in to book an appointment</p>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Email</label>
          <div class="relative">
            <i class="fa-solid fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input v-model="email" type="email" required
              class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none" placeholder="Email" />
          </div>
        </div>
        <div class="mb-4">
          <label class="text-sm font-medium mb-1 block">Password</label>
          <div class="relative">
            <!-- Lock Icon -->
            <i class="fa-solid fa-lock absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>

            <!-- Password Input -->
            <input v-model="password" :type="showPassword ? 'text' : 'password'" required
              class="w-full border border-gray-300 rounded-lg pl-10 py-2 focus:outline-none" placeholder="*******" />

            <!-- Eye Icon for Toggle -->
            <svg v-if="!showPassword" @click="togglePassword"
              class="absolute right-3 top-1/2 transform -translate-y-1/2 w-6 h-6 cursor-pointer text-gray-400"
              xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
              <path fill="currentColor"
                d="M247.31 124.76c-.35-.79-8.82-19.58-27.65-38.41C194.57 61.26 162.88 48 128 48S61.43 61.26 36.34 86.35C17.51 105.18 9 124 8.69 124.76a8 8 0 0 0 0 6.5c.35.79 8.82 19.57 27.65 38.4C61.43 194.74 93.12 208 128 208s66.57-13.26 91.66-38.34c18.83-18.83 27.3-37.61 27.65-38.4a8 8 0 0 0 0-6.5M128 192c-30.78 0-57.67-11.19-79.93-33.25A133.5 133.5 0 0 1 25 128a133.3 133.3 0 0 1 23.07-30.75C70.33 75.19 97.22 64 128 64s57.67 11.19 79.93 33.25A133.5 133.5 0 0 1 231.05 128c-7.21 13.46-38.62 64-103.05 64m0-112a48 48 0 1 0 48 48a48.05 48.05 0 0 0-48-48m0 80a32 32 0 1 1 32-32a32 32 0 0 1-32 32" />
            </svg>
            <svg v-else @click="togglePassword"
              class="absolute right-3 top-1/2 transform -translate-y-1/2 w-6 h-6 cursor-pointer text-gray-400 "
              xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <path fill="currentColor" fill-rule="evenodd"
                d="M20.53 4.53a.75.75 0 0 0-1.06-1.06l-16 16a.75.75 0 1 0 1.06 1.06l2.847-2.847c1.367.644 2.94 1.067 4.623 1.067c2.684 0 5.09-1.077 6.82-2.405c.867-.665 1.583-1.407 2.089-2.136c.492-.709.841-1.486.841-2.209s-.35-1.5-.841-2.209c-.506-.729-1.222-1.47-2.088-2.136q-.394-.303-.832-.583zM16.9 8.161l-1.771 1.771a3.75 3.75 0 0 1-5.197 5.197l-1.417 1.416A9.3 9.3 0 0 0 12 17.25c2.287 0 4.38-.923 5.907-2.095c.762-.585 1.364-1.218 1.77-1.801c.419-.604.573-1.077.573-1.354s-.154-.75-.573-1.354c-.406-.583-1.008-1.216-1.77-1.801q-.47-.361-1.008-.684m-5.87 5.87a2.25 2.25 0 0 0 3-3z"
                clip-rule="evenodd" />
              <path fill="currentColor"
                d="M12 5.25c1.032 0 2.024.16 2.951.431a.243.243 0 0 1 .1.407l-.824.825a.25.25 0 0 1-.237.067A9 9 0 0 0 12 6.75c-2.287 0-4.38.923-5.907 2.095c-.762.585-1.364 1.218-1.77 1.801c-.419.604-.573 1.077-.573 1.354s.154.75.573 1.354c.354.51.858 1.057 1.488 1.577c.116.095.127.27.02.377l-.708.709a.246.246 0 0 1-.333.016a9.5 9.5 0 0 1-1.699-1.824C2.6 13.5 2.25 12.723 2.25 12s.35-1.5.841-2.209c.506-.729 1.222-1.47 2.088-2.136C6.91 6.327 9.316 5.25 12 5.25" />
              <path fill="currentColor"
                d="M12 8.25q.178 0 .351.016c.197.019.268.254.129.394l-1.213 1.212a2.26 2.26 0 0 0-1.395 1.395L8.66 12.48c-.14.14-.375.068-.394-.129A3.75 3.75 0 0 1 12 8.25" />
            </svg>
          </div>
        </div>
        <!-- <button type="submit" :disabled="isSubmitting"
          class="w-full bg-black text-white py-3 rounded-lg text-sm font-semibold hover:bg-gray-800">
          <span v-if="isSubmitting" class="mr-2 spinner-border spinner-border-sm" role="status"
            aria-hidden="true"></span>
          Login
        </button> -->
        <button type="submit" :disabled="isSubmitting"
          class="w-full bg-black text-white py-3 rounded-lg text-sm font-semibold hover:bg-gray-800 flex items-center justify-center">
          <template v-if="isSubmitting">
            <span class="mr-2 spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          </template>
          <span v-else>Login</span>
        </button>

        <p class="text-sm font-medium pt-2 text-gray-600">
          Create a new account?
          <router-link to="/register" class="cursor-pointer text-blue-500">Click here</router-link>
        </p>
      </form>
      <div class="flex gap-4 pt-4 w-auto justify-center">
        <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300">
          <img src="https://www.google.com/favicon.ico" alt="Google" class="w-6 h-6" />
        </button>
        <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300">
          <img src="https://www.facebook.com/favicon.ico" alt="Facebook" class="w-6 h-6" />
        </button>
        <button class="flex items-center justify-center w-auto shadow-md px-9 py-2 rounded-lg border border-gray-300">
          <img src="https://www.apple.com/favicon.ico" alt="Apple" class="w-6 h-6" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import { login } from "../auth";

const router = useRouter();
const email = ref("");
const password = ref("");
const toast = useToast();
const showPassword = ref(false);
const isSubmitting = ref(false)

const togglePassword = () => {
  showPassword.value = !showPassword.value;
};
const handleLogin = async () => {
  isSubmitting.value = true;
  if (!email.value || !password.value) {
    toast.error("Please fill in all fields.");
    isSubmitting.value = false;
    return;
  } else {
    try {
      const response = await axios.post("/api/method/appointments_management.controllers.api.login_user", {
        email: email.value,
        password: password.value,
      });

      const result = response.data;

      if (result.message.code === 200) {
        login(result.message.user);
        toast.success("Login successful!");
        router.push("/");
      } else if (result.message.code === 401) {
        toast.error("Invalid password");
      } else if (result.message.code === 404) {
        toast.error("User not found");
      } else {
        toast.error(result.message || "Login failed. Please try again.");
      }
    } catch (error) {
      toast.error("An error occurred during login. Please try again later.");
      console.error("Login error:", error);
    } finally {
      isSubmitting.value = false;
    }
  }


};
</script>
<style>
.spinner-border {
  display: inline-block;
  width: 1em;
  height: 1em;
  vertical-align: middle;
  border: 2px solid transparent;
  border-top-color: white;
  border-bottom-color: red;
  border-radius: 50%;
  animation: spin 0.75s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}
</style>